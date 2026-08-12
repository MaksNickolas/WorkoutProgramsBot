from aiogram import Router, types
from aiogram.filters import Command
from keyboards.inline import main_menu, level_menu
from database.db import get_user_level, set_user_level

router = Router()


@router.message(Command("start"))
async def start_command(message: types.Message):
    user_id = message.from_user.id
    level = get_user_level(user_id)
    if not level:
        set_user_level(user_id, 1)

    await message.answer(
        "💪 Привет! Твой боевой дневник тренировок.\n\n"
        "Выбери программу:",
        reply_markup=main_menu()
    )


@router.callback_query(lambda c: c.data == "main_menu")
async def back_to_main(callback: types.CallbackQuery):
    await callback.message.edit_text(
        "Главное меню:",
        reply_markup=main_menu()
    )
    await callback.answer()


@router.callback_query(lambda c: c.data == "change_level")
async def change_level(callback: types.CallbackQuery):
    await callback.message.edit_text(
        "Выбери уровень сложности:",
        reply_markup=level_menu()
    )
    await callback.answer()


@router.callback_query(lambda c: c.data.startswith("level_"))
async def set_level(callback: types.CallbackQuery):
    level = int(callback.data.split("_")[1])
    set_user_level(callback.from_user.id, level)
    await callback.answer(f"Уровень {level} установлен!")
    await callback.message.edit_text(
        f"✅ Уровень {level} сохранен!",
        reply_markup=main_menu()
    )