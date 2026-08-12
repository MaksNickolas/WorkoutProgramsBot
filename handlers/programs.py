from aiogram import Router, types
from keyboards.inline import day_menu, exercise_buttons, finish_day_button
from data.programs import PROGRAMS, LEVELS
from database.db import get_user_level, get_daily_status

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
async def show_day(callback: types.CallbackQuery):
    _, program, day = callback.data.split("_")
    exercises = PROGRAMS[program][day]
    level = get_user_level(callback.from_user.id)
    reps = LEVELS[level]["reps"]

    text = f"📅 {day.upper()} | Уровень {level} ({LEVELS[level]['label']})\n\n"

    for ex in exercises:
        if ex['sets'] > 0:
            text += f"• {ex['name']} — {ex['sets']} подходов по {reps} раз"
            if ex['weight']:
                text += " (с весом)"
            text += "\n"
        else:
            text += f"• {ex['name']}\n"

    text += "\n⬇️ Нажми на упражнение:"

    kb = []
    for ex in exercises:
        if ex['sets'] > 0:
            kb.append([types.InlineKeyboardButton(
                text=ex['name'],
                callback_data=f"ex_{program}_{day}_{ex['name']}"
            )])
    kb.append([types.InlineKeyboardButton(text="🔙 Назад", callback_data=f"program_{program}")])

    await callback.message.edit_text(
        text,
        reply_markup=types.InlineKeyboardMarkup(inline_keyboard=kb)
    )
    await callback.answer()