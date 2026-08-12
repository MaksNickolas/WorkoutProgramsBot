from aiogram import Router, types
from database.db import get_recent_history
from data.programs import get_exercise_name
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
        exercise_name = get_exercise_name(h['exercise_id'])
        text += f"• {h['program'].upper()} {h['day'].upper()}: {exercise_name}\n"
        text += f"  {h['reps']} раз, {h['weight'] if h['weight'] else '—'} кг, {h['approaches']} подходов\n"
        text += f"  📅 {h['date']}\n\n"

    await callback.message.edit_text(text, reply_markup=main_menu())
    await callback.answer()