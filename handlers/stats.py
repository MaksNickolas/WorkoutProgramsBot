from aiogram import Router, types
from database.db import get_recent_history
from keyboards.inline import main_menu

router = Router()


@router.callback_query(lambda c: c.data == "stats")
async def show_stats(callback: types.CallbackQuery):
    history = get_recent_history(callback.from_user.id, 10)

    if not history:
        await callback.message.edit_text(
            "📊 У тебя пока нет записей. Начни тренироваться!",
            reply_markup=main_menu()
        )
        await callback.answer()
        return

    text = "📊 ПОСЛЕДНИЕ ТРЕНИРОВКИ:\n\n"
    for h in history[:5]:
        text += f"• {h[0].upper()} {h[1].upper()}: {h[2]}\n"
        text += f"  {h[4]} раз, {h[3]} кг, {h[5]} подходов\n"
        text += f"  📅 {h[6]}\n\n"

    await callback.message.edit_text(text, reply_markup=main_menu())
    await callback.answer()


@router.callback_query(lambda c: c.data.startswith("level_"))
async def set_level(callback: types.CallbackQuery):
    level = int(callback.data.split("_")[1])
    from database.db import set_user_level
    set_user_level(callback.from_user.id, level)
    await callback.answer(f"Уровень {level} установлен!")
    await callback.message.edit_text(
        f"✅ Уровень {level} сохранен!",
        reply_markup=main_menu()
    )


@router.callback_query(lambda c: c.data == "change_level")
async def change_level(callback: types.CallbackQuery):
    from keyboards.inline import level_menu
    await callback.message.edit_text(
        "Выбери уровень сложности:",
        reply_markup=level_menu()
    )
    await callback.answer()


@router.callback_query(lambda c: c.data.startswith("back_"))
async def back_to_day(callback: types.CallbackQuery):
    from handlers.programs import show_day
    _, program, day = callback.data.split("_")
    await show_day(callback)