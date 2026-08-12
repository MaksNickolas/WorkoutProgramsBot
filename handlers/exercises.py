from aiogram import Router, types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from datetime import datetime

from data.programs import PROGRAMS, LEVELS, get_exercise_name, get_expander_text
from database.db import (
    get_user_level,
    get_exercise_history,
    get_completed_exercises,
    reset_daily_status,
    get_connection,
    get_today_exercise_details,
    save_exercise_result,
    mark_exercise_completed
)
from keyboards.inline import (
    cancel_button,
    back_to_day_button,
    finish_workout_button,
    main_menu,
    get_day_keyboard
)

router = Router()


class ExerciseState(StatesGroup):
    waiting_for_approach = State()


def get_total_sets(program, day, exercise_id):
    for ex in PROGRAMS[program][day]:
        if ex['id'] == exercise_id:
            return ex['sets']
    return 0


@router.callback_query(lambda c: c.data.startswith("ex_"))
async def start_exercise(callback: types.CallbackQuery, state: FSMContext):
    _, program, day, exercise_id = callback.data.split("_", 3)
    user_id = callback.from_user.id

    # Проверяем, не выполнено ли уже
    completed = get_completed_exercises(user_id, day)
    if exercise_id in completed:
        await callback.answer("⚠️ Это упражнение уже выполнено!", show_alert=True)
        return

    exercise_name = get_exercise_name(exercise_id)
    last_result = get_exercise_history(user_id, program, day, exercise_id)
    today_details = get_today_exercise_details(user_id, program, day, exercise_id)

    # Настройки упражнения
    total_sets = 0
    has_weight = False
    for ex in PROGRAMS[program][day]:
        if ex['id'] == exercise_id:
            total_sets = ex['sets']
            has_weight = ex['weight']
            break

    await state.update_data(
        program=program,
        day=day,
        exercise_id=exercise_id,
        exercise_name=exercise_name,
        has_weight=has_weight,
        total_sets=total_sets,
        current_set=1,
        approaches_data=[]
    )

    text = f"🏋️ {exercise_name}\n\n"

    # === ПОКАЗЫВАЕМ ИСТОРИЮ ===
    if today_details:
        text += f"📊 Твоя тренировка сегодня ({today_details[0]['date']}):\n"
        for i, app in enumerate(today_details, 1):
            weight_str = f"{app['weight']} кг" if has_weight and app['weight'] else "—"
            text += f"  Подход {i}: {app['reps']} раз × {weight_str}\n"
        text += "\n"
    elif last_result and last_result.get('date') != "—" and last_result.get('reps', 0) > 0:
        text += f"📊 Последний результат (другая тренировка):\n"
        weight_str = f"{last_result['weight']} кг" if has_weight and last_result.get('weight', 0) else "—"
        text += f"  Вес: {weight_str}, Повторов: {last_result['reps']}, Подходов: {last_result['approaches']}\n"
        text += f"  📅 {last_result['date']}\n\n"
    else:
        text += "🔄 Это первая тренировка этого упражнения.\n\n"

    # === ПЕРВЫЙ ПОДХОД ===
    text += f"🔹 ПОДХОД №1 из {total_sets}\n\n"
    if has_weight:
        text += "✏️ Введите вес (кг) и повторения через пробел:\nПример: 20 10"
    else:
        text += "✏️ Введите количество повторений:\nПример: 10"

    await callback.message.edit_text(text, reply_markup=cancel_button(program, day))
    await state.set_state(ExerciseState.waiting_for_approach)
    await callback.answer()


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
    raw_text = message.text.strip()

    # === ПАРСИНГ ===
    if has_weight:
        parts = raw_text.split()
        if len(parts) != 2:
            await message.answer("❌ Введи ДВА числа (вес и повторения) через пробел. Например: 20 10")
            return
        try:
            weight = float(parts[0].replace(",", "."))
            reps = int(parts[1])
            if weight < 0 or reps < 1: raise ValueError
        except:
            await message.answer("❌ Ошибка ввода. Пример: 20 10")
            return
    else:
        try:
            reps = int(raw_text)
            weight = 0
            if reps < 1: raise ValueError
        except:
            await message.answer("❌ Введи целое число. Например: 10")
            return

    # Сохраняем подход в список
    approaches_data.append({"weight": weight, "reps": reps})

    # === ПРОВЕРКА: ПОСЛЕДНИЙ ЛИ ЭТО ПОДХОД ===
    if current_set >= total_sets:
        # 1. Сохраняем ВСЕ подходы в БД
        for app in approaches_data:
            save_exercise_result(user_id, program, day, exercise_id, app['weight'], app['reps'], 1)

        # 2. Отмечаем упражнение как завершенное
        mark_exercise_completed(user_id, day, exercise_id, total_sets)
        await state.clear()

        # 3. Проверяем, все ли упражнения дня выполнены
        completed = get_completed_exercises(user_id, day)
        total_exercises = len([ex for ex in PROGRAMS[program][day] if ex['sets'] > 0])

        # 4. Отчет по подходам
        summary = f"✅ {exercise_name} — {total_sets} подходов:\n"
        for i, app in enumerate(approaches_data, 1):
            w_str = f"{app['weight']} кг" if has_weight else "—"
            summary += f"  {i}. {app['reps']} раз × {w_str}\n"

        # 5. Отправка результата
        if len(completed) >= total_exercises:
            await message.answer(
                f"{summary}\n\n🎉 ВСЕ УПРАЖНЕНИЯ ДНЯ ВЫПОЛНЕНЫ!",
                reply_markup=finish_workout_button(program, day)
            )
        else:
            await message.answer(
                f"{summary}\n\nОсталось упражнений: {total_exercises - len(completed)}",
                reply_markup=back_to_day_button(program, day)
            )
        return

    # === ЕСЛИ НЕ ПОСЛЕДНИЙ — ПРОСИМ СЛЕДУЮЩИЙ ===
    await state.update_data(current_set=current_set + 1, approaches_data=approaches_data)
    next_set = current_set + 1

    response_text = f"🏋️ {exercise_name}\n\n"
    response_text += f"✅ Подход №{current_set} сохранён ({reps} раз"
    if has_weight: response_text += f" × {weight} кг"
    response_text += ")\n\n"
    response_text += f"🔹 ПОДХОД №{next_set} из {total_sets}\n\n"

    if has_weight:
        response_text += "✏️ Введите вес (кг) и повторения через пробел:\nПример: 20 10"
    else:
        response_text += "✏️ Введите количество повторений:\nПример: 10"

    await message.answer(response_text, reply_markup=cancel_button(program, day))


@router.callback_query(lambda c: c.data.startswith("cancel_exercise_"))
async def cancel_exercise(callback: types.CallbackQuery, state: FSMContext):
    await state.clear()
    _, program, day = callback.data.split("_", 2)
    user_id = callback.from_user.id

    exercises = PROGRAMS[program][day]
    completed = get_completed_exercises(user_id, day)
    level = get_user_level(user_id)
    reps = LEVELS[level]["reps"]

    text = f"📅 {day.upper()} | Уровень {level} ({LEVELS[level]['label']})\n\nВыбери упражнение:\n\n"
    for ex in exercises:
        ex_id = ex['id']
        ex_name = get_exercise_name(ex_id)
        if ex['sets'] == 0:
            text += f"⏸️ {ex_name}\n"
        elif ex_id in completed:
            text += f"✅ {ex_name} (выполнено)\n"
        else:
            ex_reps = ex.get('reps_per_set', reps)
            text += f"⬜ {ex_name} — {ex['sets']} подходов по {ex_reps} раз"
            if ex['weight']: text += " (с весом)"
            text += "\n"

    expander_text = get_expander_text(program, day)
    if expander_text and day not in ["чт", "вс"]:
        text += f"\n---\n{expander_text}"

    await callback.message.edit_text(text, reply_markup=get_day_keyboard(program, day, completed))
    await callback.answer()


@router.callback_query(lambda c: c.data.startswith("finish_workout_"))
async def finish_workout(callback: types.CallbackQuery):
    _, program, day = callback.data.split("_", 2)
    reset_daily_status(callback.from_user.id)
    await callback.message.edit_text(
        f"🎉 Тренировка на {day.upper()} завершена!\n\nОтличная работа! 💪",
        reply_markup=main_menu()
    )
    await callback.answer()