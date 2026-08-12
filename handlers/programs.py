from aiogram import Router, types
from keyboards.inline import day_menu, get_day_keyboard
from data.programs import PROGRAMS, LEVELS
from database.db import get_user_level, get_completed_exercises

router = Router()


@router.callback_query(lambda c: c.data.startswith("program_"))
async def choose_program(callback: types.CallbackQuery):
    program = callback.data.split("_")[1]
    await callback.message.edit_text(
        f"Выбрано: {program.upper()}\nВыбери день:",
        reply_markup=day_menu(program)
    )
    await callback.answer()


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