from aiogram import Router, types
from data.programs import PROGRAMS, LEVELS
from database.db import (
    get_user_level, get_last_history, get_daily_status,
    update_daily_status, save_history
)
from keyboards.inline import exercise_buttons, finish_day_button

router = Router()


@router.callback_query(lambda c: c.data.startswith("ex_"))
async def start_exercise(callback: types.CallbackQuery):
    _, program, day, exercise = callback.data.split("_", 3)
    user_id = callback.from_user.id
    level = get_user_level(user_id)
    reps = LEVELS[level]["reps"]

    # Прошлая тренировка
    last = get_last_history(user_id, program, day, exercise)

    text = f"🏋️ {exercise}\n\n"
    text += f"Уровень: {level} ({LEVELS[level]['label']}) — {reps} повторений за подход\n"

    if last:
        text += f"\n📊 ПРОШЛАЯ ТРЕНИРОВКА:\n"
        text += f"Вес: {last[0] if last[0] else '—'} кг\n"
        text += f"Повторов: {last[1]}\n"
        text += f"Подходов: {last[2]}\n"
    else:
        text += "\n🔄 Это первая тренировка этого упражнения."

    # Текущий статус
    status = get_daily_status(user_id, day, exercise)
    if status:
        approaches_done = status[1]
        total_sets = 0
        for ex in PROGRAMS[program][day]:
            if ex['name'] == exercise:
                total_sets = ex['sets']
                break
        text += f"\n\n✅ Выполнено подходов: {approaches_done}/{total_sets}"
        if status[0]:
            text += "\n✔️ Упражнение ЗАВЕРШЕНО!"

    await callback.message.edit_text(
        text,
        reply_markup=exercise_buttons(program, day, exercise)
    )
    await callback.answer()


@router.callback_query(lambda c: c.data.startswith("set_"))
async def do_set(callback: types.CallbackQuery):
    _, program, day, exercise = callback.data.split("_", 3)
    user_id = callback.from_user.id

    update_daily_status(user_id, day, exercise, approaches_done=True)

    await callback.answer("✅ Подход засчитан!")
    await start_exercise(callback)


@router.callback_query(lambda c: c.data.startswith("finish_"))
async def finish_exercise(callback: types.CallbackQuery):
    _, program, day, exercise = callback.data.split("_", 3)
    user_id = callback.from_user.id
    level = get_user_level(user_id)
    reps = LEVELS[level]["reps"]

    status = get_daily_status(user_id, day, exercise)
    if not status or status[1] == 0:
        await callback.answer("⚠️ Сначала выполни хотя бы один подход!", show_alert=True)
        return

    # Сохраняем в историю
    save_history(user_id, program, day, exercise, 0, reps, status[1])
    update_daily_status(user_id, day, exercise, completed=1)

    await callback.answer("🏁 Упражнение завершено!")

    # Проверяем все ли упражнения дня завершены
    exercises = PROGRAMS[program][day]
    all_done = True
    for ex in exercises:
        if ex['sets'] > 0:
            st = get_daily_status(user_id, day, ex['name'])
            if not st or st[0] == 0:
                all_done = False
                break

    if all_done and any(ex['sets'] > 0 for ex in exercises):
        await callback.message.edit_text(
            "🔥 Все упражнения дня выполнены! Нажми кнопку, чтобы завершить день.",
            reply_markup=finish_day_button(program, day)
        )
    else:
        await start_exercise(callback)


@router.callback_query(lambda c: c.data.startswith("finish_day_"))
async def finish_day(callback: types.CallbackQuery):
    _, program, day = callback.data.split("_", 2)
    await callback.answer("🎉 Тренировка завершена!")
    await callback.message.edit_text(
        f"✅ День {day.upper()} полностью завершен!\n\nЗавтра новая тренировка. Ты молодец! 💪",
        reply_markup=main_menu()
    )