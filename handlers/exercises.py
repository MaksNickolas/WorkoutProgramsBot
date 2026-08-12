from aiogram import Router, types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from data.programs import PROGRAMS, LEVELS, get_exercise_name, get_expander_text
from database.db import (
    get_user_level,
    get_exercise_history,
    get_completed_exercises,
    reset_daily_status,
    get_connection
)
from keyboards.inline import (
    cancel_button,
    back_to_day_button,
    finish_workout_button,
    main_menu
)

router = Router()


# === СОСТОЯНИЯ ДЛЯ ВВОДА ===
class ExerciseState(StatesGroup):
    waiting_for_approach = State()  # Ожидание ввода веса и повторений для подхода


# === ВСПОМОГАТЕЛЬНАЯ ФУНКЦИЯ: ПОЛУЧИТЬ ОБЩЕЕ КОЛИЧЕСТВО ПОДХОДОВ ===
def get_total_sets(program, day, exercise_id):
    for ex in PROGRAMS[program][day]:
        if ex['id'] == exercise_id:
            return ex['sets']
    return 0


# === ОБРАБОТЧИК: НАЖАТИЕ НА УПРАЖНЕНИЕ ===
@router.callback_query(lambda c: c.data.startswith("ex_"))
async def start_exercise(callback: types.CallbackQuery, state: FSMContext):
    _, program, day, exercise_id = callback.data.split("_", 3)
    user_id = callback.from_user.id

    # Проверяем, не выполнено ли уже
    completed = get_completed_exercises(user_id, day)
    if exercise_id in completed:
        await callback.answer("⚠️ Это упражнение уже выполнено!", show_alert=True)
        return

    # Получаем красивое название
    exercise_name = get_exercise_name(exercise_id)

    # Получаем предыдущий результат
    last_result = get_exercise_history(user_id, program, day, exercise_id)

    # Находим настройки упражнения
    exercise_config = None
    total_sets = 0
    has_weight = False
    for ex in PROGRAMS[program][day]:
        if ex['id'] == exercise_id:
            exercise_config = ex
            total_sets = ex['sets']
            has_weight = ex['weight']
            break

    # Сохраняем в FSM
    await state.update_data(
        program=program,
        day=day,
        exercise_id=exercise_id,
        exercise_name=exercise_name,
        has_weight=has_weight,
        total_sets=total_sets,
        current_set=1,
        approaches_data=[]  # Сюда будем складывать каждый подход
    )

    text = f"🏋️ {exercise_name}\n\n"

    # Показываем прошлый результат
    if last_result:
        text += f"📊 ПОСЛЕДНИЙ РЕЗУЛЬТАТ:\n"
        text += f"Вес: {last_result['weight'] if last_result['weight'] else '—'} кг\n"
        text += f"Повторов: {last_result['reps']}\n"
        text += f"Подходов: {last_result['approaches']}\n"
        text += f"📅 {last_result['date']}\n\n"
    else:
        text += "🔄 Это первая тренировка этого упражнения.\n\n"

    # Запрашиваем первый подход
    text += f"🔹 ПОДХОД №1 из {total_sets}\n\n"

    if has_weight:
        text += "✏️ Введите вес (в кг) и количество повторений через пробел:\n"
        text += "Например: 20 10"
    else:
        text += "✏️ Введите количество повторений:\n"
        text += "Например: 10"

    await callback.message.edit_text(
        text,
        reply_markup=cancel_button(program, day)
    )
    await state.set_state(ExerciseState.waiting_for_approach)
    await callback.answer()


# === ОБРАБОТЧИК: ВВОД ПОДХОДА ===
@router.message(ExerciseState.waiting_for_approach)
async def process_approach(message: types.Message, state: FSMContext):
    data = await state.get_data()
    program = data['program']
    day = data['day']
    exercise_id = data['exercise_id']
    exercise_name = data['exercise_name']
    has_weight = data['has_weight']
    total_sets = data['total_sets']
    current_set = data['current_set']
    approaches_data = data.get('approaches_data', [])

    user_id = message.from_user.id
    text = message.text.strip()

    # Парсим ввод
    if has_weight:
        parts = text.split()
        if len(parts) != 2:
            await message.answer(
                "❌ Введи вес и повторения через пробел.\n"
                "Например: 20 10"
            )
            return
        try:
            weight = float(parts[0].replace(",", "."))
            reps = int(parts[1])
            if weight < 0 or reps < 1:
                raise ValueError
        except:
            await message.answer(
                "❌ Введи корректные числа.\n"
                "Например: 20 10"
            )
            return
    else:
        try:
            reps = int(text)
            weight = 0
            if reps < 1:
                raise ValueError
        except:
            await message.answer(
                "❌ Введи целое число.\n"
                "Например: 10"
            )
            return

    # Сохраняем подход
    approaches_data.append({"weight": weight, "reps": reps})

    # Проверяем, последний ли подход
    if current_set >= total_sets:
        # Сохраняем все подходы в базу
        conn = get_connection()
        cursor = conn.cursor()

        # Удаляем старый результат за сегодня
        cursor.execute("""
            DELETE FROM history 
            WHERE user_id=? AND program=? AND day=? AND exercise_id=? 
            AND date LIKE ?
        """, (user_id, program, day, exercise_id, datetime.now().strftime("%Y-%m-%d") + "%"))

        # Сохраняем каждый подход как отдельную запись
        for approach in approaches_data:
            cursor.execute("""
                INSERT INTO history (user_id, program, day, exercise_id, weight, reps, approaches, date)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (user_id, program, day, exercise_id, approach['weight'], approach['reps'], 1,
                  datetime.now().strftime("%Y-%m-%d %H:%M")))

        # Отмечаем упражнение как выполненное
        cursor.execute("""
            INSERT INTO daily_status (user_id, day, exercise_id, completed, approaches_done)
            VALUES (?, ?, ?, 1, ?)
            ON CONFLICT(user_id, day, exercise_id) DO UPDATE SET 
                completed = 1,
                approaches_done = excluded.approaches_done
        """, (user_id, day, exercise_id, total_sets))

        conn.commit()
        await state.clear()

        # Проверяем, все ли упражнения выполнены
        completed = get_completed_exercises(user_id, day)
        exercises = PROGRAMS[program][day]
        total_exercises = len([ex for ex in exercises if ex['sets'] > 0])

        # Формируем итоговый отчет
        summary = f"✅ {exercise_name} — {total_sets} подходов:\n"
        for i, app in enumerate(approaches_data, 1):
            weight_str = f"{app['weight']} кг" if has_weight else "—"
            summary += f"  {i}. {app['reps']} раз × {weight_str}\n"

        if len(completed) >= total_exercises:
            await message.answer(
                f"{summary}\n"
                f"🎉 ВСЕ УПРАЖНЕНИЯ ДНЯ ЗАВЕРШЕНЫ!",
                reply_markup=finish_workout_button(program, day)
            )
        else:
            await message.answer(
                f"{summary}\n\n"
                f"Осталось упражнений: {total_exercises - len(completed)}",
                reply_markup=back_to_day_button(program, day)
            )
    else:
        # Сохраняем прогресс и запрашиваем следующий подход
        await state.update_data(
            current_set=current_set + 1,
            approaches_data=approaches_data
        )

        next_set = current_set + 1
        text = f"🏋️ {exercise_name}\n\n"
        text += f"✅ Подход №{current_set} сохранен: {reps} раз"
        if has_weight:
            text += f" × {weight} кг"
        text += "\n\n"
        text += f"🔹 ПОДХОД №{next_set} из {total_sets}\n\n"

        if has_weight:
            text += "✏️ Введите вес (в кг) и количество повторений через пробел:\n"
            text += "Например: 20 10"
        else:
            text += "✏️ Введите количество повторений:\n"
            text += "Например: 10"

        await message.answer(
            text,
            reply_markup=cancel_button(program, day)
        )


# === ОТМЕНА ===
@router.callback_query(lambda c: c.data.startswith("cancel_exercise_"))
async def cancel_exercise(callback: types.CallbackQuery, state: FSMContext):
    await state.clear()
    _, program, day = callback.data.split("_", 2)
    user_id = callback.from_user.id

    exercises = PROGRAMS[program][day]
    completed = get_completed_exercises(user_id, day)
    level = get_user_level(user_id)
    reps = LEVELS[level]["reps"]

    text = f"📅 {day.upper()} | Уровень {level} ({LEVELS[level]['label']})\n\n"
    text += "Выбери упражнение:\n\n"

    for ex in exercises:
        exercise_id = ex['id']
        exercise_name = get_exercise_name(exercise_id)

        if ex['sets'] == 0:
            text += f"⏸️ {exercise_name}\n"
        elif exercise_id in completed:
            text += f"✅ {exercise_name} (выполнено)\n"
        else:
            ex_reps = ex.get('reps_per_set', reps)
            text += f"⬜ {exercise_name} — {ex['sets']} подходов по {ex_reps} раз"
            if ex['weight']:
                text += " (с весом)"
            text += "\n"

    from keyboards.inline import get_day_keyboard
    await callback.message.edit_text(
        text,
        reply_markup=get_day_keyboard(program, day, completed)
    )
    await callback.answer()


# === ЗАВЕРШЕНИЕ ТРЕНИРОВКИ ===
@router.callback_query(lambda c: c.data.startswith("finish_workout_"))
async def finish_workout(callback: types.CallbackQuery):
    _, program, day = callback.data.split("_", 2)
    user_id = callback.from_user.id

    reset_daily_status(user_id)

    await callback.message.edit_text(
        f"🎉 Тренировка на {day.upper()} завершена!\n\n"
        f"Отличная работа! 💪\n"
        f"Завтра новая тренировка.",
        reply_markup=main_menu()
    )
    await callback.answer()