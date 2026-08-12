from aiogram import Router, types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from data.programs import PROGRAMS, LEVELS, get_exercise_name, get_expander_text
from database.db import (
    get_user_level,
    get_exercise_history,
    get_completed_exercises,
    reset_daily_status,
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
    waiting_for_data = State()


@router.callback_query(lambda c: c.data.startswith("ex_"))
async def start_exercise(callback: types.CallbackQuery, state: FSMContext):
    _, program, day, exercise_id = callback.data.split("_", 3)
    user_id = callback.from_user.id

    # Проверяем, не выполнено ли уже
    completed = get_completed_exercises(user_id, day)
    if exercise_id in completed:
        await callback.answer("⚠️ Упражнение уже выполнено!", show_alert=True)
        return

    exercise_name = get_exercise_name(exercise_id)
    last_result = get_exercise_history(user_id, program, day, exercise_id)

    # Проверяем, есть ли вес у упражнения
    has_weight = False
    for ex in PROGRAMS[program][day]:
        if ex['id'] == exercise_id:
            has_weight = ex['weight']
            break

    # Сохраняем данные в FSM
    await state.update_data(
        program=program,
        day=day,
        exercise_id=exercise_id,
        exercise_name=exercise_name,
        has_weight=has_weight
    )

    text = f"🏋️ {exercise_name}\n\n"

    # Показываем последний результат
    if last_result and last_result.get('date') != "—":
        weight_str = f"{last_result['weight']} кг" if has_weight and last_result.get('weight', 0) else "—"
        text += f"📊 Последний раз:\n"
        text += f"  Вес: {weight_str}\n"
        text += f"  Повторов: {last_result.get('reps', 0)}\n"
        text += f"  Подходов: {last_result.get('approaches', 0)}\n"
        text += f"  📅 {last_result.get('date', '—')}\n\n"
    else:
        text += "🔄 Это первая тренировка.\n\n"

    # Формат ввода
    text += "✏️ Введите данные через пробел:\n"
    if has_weight:
        text += "Формат: вес повторения подходы\n"
        text += "Пример: 20 10 4"
    else:
        text += "Формат: повторения подходы\n"
        text += "Пример: 10 4"

    await callback.message.edit_text(
        text,
        reply_markup=cancel_button(program, day)
    )
    await state.set_state(ExerciseState.waiting_for_data)
    await callback.answer()


@router.message(ExerciseState.waiting_for_data)
async def process_data(message: types.Message, state: FSMContext):
    data = await state.get_data()
    program = data['program']
    day = data['day']
    exercise_id = data['exercise_id']
    exercise_name = data['exercise_name']
    has_weight = data['has_weight']

    user_id = message.from_user.id
    raw = message.text.strip().split()

    # Парсинг ввода
    try:
        if has_weight:
            if len(raw) != 3:
                await message.answer(
                    "❌ Нужно 3 числа: вес повторения подходы.\n"
                    "Пример: 20 10 4"
                )
                return
            weight = float(raw[0].replace(",", "."))
            reps = int(raw[1])
            approaches = int(raw[2])
        else:
            if len(raw) != 2:
                await message.answer(
                    "❌ Нужно 2 числа: повторения подходы.\n"
                    "Пример: 10 4"
                )
                return
            weight = 0
            reps = int(raw[0])
            approaches = int(raw[1])

        if reps < 1 or approaches < 1 or weight < 0:
            raise ValueError
    except ValueError:
        await message.answer("❌ Ошибка ввода. Проверь формат.")
        return

    # Сохраняем результат
    save_exercise_result(user_id, program, day, exercise_id, weight, reps, approaches)
    mark_exercise_completed(user_id, day, exercise_id, approaches)

    await state.clear()

    # Проверяем, все ли упражнения выполнены
    completed = get_completed_exercises(user_id, day)
    total_exercises = len([ex for ex in PROGRAMS[program][day] if ex['sets'] > 0])

    summary = f"✅ {exercise_name}: {approaches} подходов × {reps} раз"
    if has_weight:
        summary += f" × {weight} кг"

    # Возвращаем к списку упражнений дня
    if len(completed) >= total_exercises:
        await message.answer(
            f"{summary}\n\n🎉 ВСЕ УПРАЖНЕНИЯ ВЫПОЛНЕНЫ!",
            reply_markup=finish_workout_button(program, day)
        )
    else:
        # Показываем обновленный список упражнений
        await show_day_exercises_message(
            message,
            program,
            day,
            user_id,
            text=f"{summary}\n\nОсталось: {total_exercises - len(completed)} упражнений"
        )


async def show_day_exercises_message(message: types.Message, program: str, day: str, user_id: int, text: str = None):
    """Отображает список упражнений дня (используется после ввода)"""
    exercises = PROGRAMS[program][day]
    completed = get_completed_exercises(user_id, day)
    level = get_user_level(user_id)
    reps = LEVELS[level]["reps"]

    if text is None:
        text = f"📅 {day.upper()} | Уровень {level} ({LEVELS[level]['label']})\n\n"
        text += "Выбери упражнение:\n\n"
    else:
        text += f"\n\n📅 {day.upper()} | Уровень {level} ({LEVELS[level]['label']})\n\n"
        text += "Выбери упражнение:\n\n"

    for ex in exercises:
        ex_id = ex['id']
        ex_name = get_exercise_name(ex_id)
        if ex['sets'] == 0:
            text += f"⏸️ {ex_name}\n"
        elif ex_id in completed:
            text += f"✅ {ex_name} (выполнено)\n"
        else:
            text += f"⬜ {ex_name} — {ex['sets']} подходов\n"

    expander_text = get_expander_text(program, day)
    if expander_text and day not in ["чт", "вс"]:
        text += f"\n---\n{expander_text}"

    await message.answer(
        text,
        reply_markup=get_day_keyboard(program, day, completed)
    )


@router.callback_query(lambda c: c.data.startswith("cancel_exercise_"))
async def cancel_exercise(callback: types.CallbackQuery, state: FSMContext):
    """Отмена ввода → возврат к списку упражнений"""
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
        ex_id = ex['id']
        ex_name = get_exercise_name(ex_id)
        if ex['sets'] == 0:
            text += f"⏸️ {ex_name}\n"
        elif ex_id in completed:
            text += f"✅ {ex_name} (выполнено)\n"
        else:
            text += f"⬜ {ex_name} — {ex['sets']} подходов\n"

    expander_text = get_expander_text(program, day)
    if expander_text and day not in ["чт", "вс"]:
        text += f"\n---\n{expander_text}"

    await callback.message.edit_text(
        text,
        reply_markup=get_day_keyboard(program, day, completed)
    )
    await callback.answer()


@router.callback_query(lambda c: c.data.startswith("finish_workout_"))
async def finish_workout(callback: types.CallbackQuery):
    _, program, day = callback.data.split("_", 2)
    reset_daily_status(callback.from_user.id)

    await callback.message.edit_text(
        f"🎉 Тренировка на {day.upper()} завершена!\n\n"
        f"Отличная работа! 💪",
        reply_markup=main_menu()
    )
    await callback.answer()