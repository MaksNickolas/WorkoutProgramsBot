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
        text += f"• {h['program'].upper()} {h['day'].upper()}: {h['exercise']}\n"
        text += f"  {h['reps']} раз, {h['weight'] if h['weight'] else '—'} кг, {h['approaches']} подходов\n"
        text += f"  📅 {h['date']}\n\n"

    await callback.message.edit_text(text, reply_markup=main_menu())
    await callback.answer()