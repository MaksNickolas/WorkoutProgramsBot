from aiogram import Router, types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from data.programs import PROGRAMS, LEVELS
from database.db import (
    get_user_level,
    get_exercise_history,
    save_exercise_result,
    get_completed_exercises,
    reset_daily_status
)
from keyboards.inline import (
    cancel_button,
    back_to_day_button,
    finish_workout_button,
    get_day_keyboard,
    main_menu
)

router = Router()


# === СОСТОЯНИЯ ДЛЯ ВВОДА ===
class ExerciseState(StatesGroup):
    waiting_for_weight = State()
    waiting_for_reps = State()
    waiting_for_approaches = State()


# === ОБРАБОТЧИК: НАЖАТИЕ НА УПРАЖНЕНИЕ ===
@router.callback_query(lambda c: c.data.startswith("ex_"))
async def start_exercise(callback: types.CallbackQuery, state: FSMContext):
    _, program, day, exercise = callback.data.split("_", 3)
    user_id = callback.from_user.id

    # Проверяем, не выполнено ли уже
    completed = get_completed_exercises(user_id, day)
    if exercise in completed:
        await callback.answer("⚠️ Это упражнение уже выполнено!", show_alert=True)
        return

    # Получаем предыдущий результат
    last_result = get_exercise_history(user_id, program, day, exercise)

    # Сохраняем в FSM
    await state.update_data(
        program=program,
        day=day,
        exercise=exercise,
        last_result=last_result
    )

    # Находим настройки упражнения
    exercise_config = None
    for ex in PROGRAMS[program][day]:
        if ex['name'] == exercise:
            exercise_config = ex
            break

    text = f"🏋️ {exercise}\n\n"

    # Показываем прошлый результат
    if last_result:
        text += f"📊 ПОСЛЕДНИЙ РЕЗУЛЬТАТ:\n"
        text += f"Вес: {last_result['weight'] if last_result['weight'] else '—'} кг\n"
        text += f"Повторов: {last_result['reps']}\n"
        text += f"Подходов: {last_result['approaches']}\n"
        text += f"📅 {last_result['date']}\n\n"
    else:
        text += "🔄 Это первая тренировка этого упражнения.\n\n"

    if exercise_config['weight']:
        text += "✏️ Введите вес (в кг):\nНапример: 20"
        await state.set_state(ExerciseState.waiting_for_weight)
    else:
        text += "✏️ Введите количество повторений за подход:\nНапример: 10"
        await state.set_state(ExerciseState.waiting_for_reps)

    await callback.message.edit_text(
        text,
        reply_markup=cancel_button(program, day)
    )
    await callback.answer()


# === ВВОД ВЕСА ===
@router.message(ExerciseState.waiting_for_weight)
async def process_weight(message: types.Message, state: FSMContext):
    try:
        weight = float(message.text.replace(",", "."))
        if weight < 0:
            raise ValueError
    except:
        await message.answer("❌ Введи число (например: 20 или 25.5)")
        return

    await state.update_data(weight=weight)
    await state.set_state(ExerciseState.waiting_for_reps)

    await message.answer(
        "✏️ Введите количество повторений за подход:\nНапример: 10"
    )


# === ВВОД ПОВТОРЕНИЙ ===
@router.message(ExerciseState.waiting_for_reps)
async def process_reps(message: types.Message, state: FSMContext):
    try:
        reps = int(message.text)
        if reps < 1:
            raise ValueError
    except:
        await message.answer("❌ Введи целое число (например: 10)")
        return

    await state.update_data(reps=reps)
    await state.set_state(ExerciseState.waiting_for_approaches)

    data = await state.get_data()
    program = data['program']
    day = data['day']
    exercise = data['exercise']

    default_approaches = 0
    for ex in PROGRAMS[program][day]:
        if ex['name'] == exercise:
            default_approaches = ex['sets']
            break

    await message.answer(
        f"✏️ Введите количество подходов:\n"
        f"По умолчанию: {default_approaches}\n"
        f"Например: {default_approaches}"
    )


# === ВВОД ПОДХОДОВ ===
@router.message(ExerciseState.waiting_for_approaches)
async def process_approaches(message: types.Message, state: FSMContext):
    try:
        approaches = int(message.text)
        if approaches < 1:
            raise ValueError
    except:
        await message.answer("❌ Введи целое число (например: 4)")
        return

    data = await state.get_data()
    program = data['program']
    day = data['day']
    exercise = data['exercise']
    weight = data.get('weight', 0)
    reps = data['reps']
    user_id = message.from_user.id

    # Сохраняем результат
    save_exercise_result(user_id, program, day, exercise, weight, reps, approaches)

    # Проверяем, все ли упражнения выполнены
    completed = get_completed_exercises(user_id, day)
    exercises = PROGRAMS[program][day]
    total_exercises = len([ex for ex in exercises if ex['sets'] > 0])

    await state.clear()

    if len(completed) >= total_exercises:
        await message.answer(
            f"✅ Упражнение '{exercise}' выполнено!\n"
            f"🎉 Все упражнения дня завершены!",
            reply_markup=finish_workout_button(program, day)
        )
    else:
        await message.answer(
            f"✅ Упражнение '{exercise}' выполнено!\n\n"
            f"Осталось упражнений: {total_exercises - len(completed)}",
            reply_markup=back_to_day_button(program, day)
        )


# === ОТМЕНА ===
@router.callback_query(lambda c: c.data.startswith("cancel_exercise_"))
async def cancel_exercise(callback: types.CallbackQuery, state: FSMContext):
    await state.clear()
    _, program, day = callback.data.split("_", 2)
    await show_day_exercises(callback)


# === ВОЗВРАТ К СПИСКУ ===
@router.callback_query(lambda c: c.data.startswith("day_"))
async def show_day_exercises(callback: types.CallbackQuery):
    _, program, day = callback.data.split("_")
    user_id = callback.from_user.id

    exercises = PROGRAMS[program][day]
    completed = get_completed_exercises(user_id, day)
    level = get_user_level(user_id)
    reps = LEVELS[level]["reps"]

    text = f"📅 {day.upper()} | Уровень {level} ({LEVELS[level]['label']})\n\n"
    text += "Выбери упражнение:\n\n"

    for ex in exercises:
        if ex['sets'] == 0:
            text += f"⏸️ {ex['name']}\n"
        elif ex['name'] in completed:
            text += f"✅ {ex['name']} (выполнено)\n"
        else:
            text += f"⬜ {ex['name']} — {ex['sets']} подходов по {reps} раз"
            if ex['weight']:
                text += " (с весом)"
            text += "\n"

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