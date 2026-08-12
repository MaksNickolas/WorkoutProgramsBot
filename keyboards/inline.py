from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from data.programs import PROGRAMS, DAYS

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

def exercise_buttons(program, day, exercise):
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="✅ Выполнил подход", callback_data=f"set_{program}_{day}_{exercise}")],
        [InlineKeyboardButton(text="🏁 Завершить упражнение", callback_data=f"finish_{program}_{day}_{exercise}")],
        [InlineKeyboardButton(text="🔙 Назад", callback_data=f"back_{program}_{day}")]
    ])

def finish_day_button(program, day):
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🎉 ЗАВЕРШИТЬ ДЕНЬ", callback_data=f"finish_day_{program}_{day}")]
    ])

def level_menu():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="1️⃣ Начальный (8 повторений)", callback_data="level_1")],
        [InlineKeyboardButton(text="2️⃣ Средний (12 повторений)", callback_data="level_2")],
        [InlineKeyboardButton(text="3️⃣ Продвинутый (15 повторений)", callback_data="level_3")],
        [InlineKeyboardButton(text="🔙 Назад", callback_data="main_menu")]
    ])