from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from data.programs import PROGRAMS, DAYS, get_exercise_name


def main_menu():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🏠 Дом", callback_data="program_дом")],
        [InlineKeyboardButton(text="🌳 Улица", callback_data="program_улица")],
        [InlineKeyboardButton(text="🌿 Дача", callback_data="program_дача")],
        [InlineKeyboardButton(text="⚙️ Уровень (1-3)", callback_data="change_level")],
        [InlineKeyboardButton(text="📊 Моя статистика", callback_data="stats")]
    ])


def day_menu(program):
    kb = []
    for day in DAYS:
        kb.append([InlineKeyboardButton(text=day.upper(), callback_data=f"day_{program}_{day}")])
    kb.append([InlineKeyboardButton(text="🔙 Назад", callback_data="main_menu")])
    return InlineKeyboardMarkup(inline_keyboard=kb)


def level_menu():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="1️⃣ Начальный (8 повторений)", callback_data="level_1")],
        [InlineKeyboardButton(text="2️⃣ Средний (12 повторений)", callback_data="level_2")],
        [InlineKeyboardButton(text="3️⃣ Продвинутый (15 повторений)", callback_data="level_3")],
        [InlineKeyboardButton(text="🔙 Назад", callback_data="main_menu")]
    ])


def get_day_keyboard(program, day, completed_exercises):
    exercises = PROGRAMS[program][day]
    kb = []
    for ex in exercises:
        if ex['sets'] == 0:
            continue
        ex_id = ex['id']
        if ex_id not in completed_exercises:
            kb.append([InlineKeyboardButton(
                text=f"💪 {get_exercise_name(ex_id)}",
                callback_data=f"ex_{program}_{day}_{ex_id}"
            )])

    if not kb:
        kb.append([InlineKeyboardButton(
            text="✅ Завершить тренировку",
            callback_data=f"finish_workout_{program}_{day}"
        )])

    kb.append([InlineKeyboardButton(text="🔙 Назад", callback_data=f"program_{program}")])
    return InlineKeyboardMarkup(inline_keyboard=kb)


def cancel_button(program, day):
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🔙 Отмена", callback_data=f"cancel_exercise_{program}_{day}")]
    ])


def back_to_day_button(program, day):
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📋 Вернуться к списку", callback_data=f"day_{program}_{day}")]
    ])


def finish_workout_button(program, day):
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="✅ Завершить тренировку", callback_data=f"finish_workout_{program}_{day}")]
    ])