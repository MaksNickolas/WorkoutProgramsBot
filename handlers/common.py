from aiogram import Router, types
from aiogram.filters import Command
from keyboards.inline import main_menu
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