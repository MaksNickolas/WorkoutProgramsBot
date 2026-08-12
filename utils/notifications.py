import asyncio
from datetime import datetime
from aiogram import Bot
from config import ADMIN_ID


async def daily_notification(bot: Bot):
    """Отправляет уведомления в 8:00"""
    while True:
        now = datetime.now()

        if now.hour == 8 and now.minute == 0:
            try:
                await bot.send_message(
                    chat_id=ADMIN_ID,
                    text="🌅 Доброе утро! Сегодня у тебя тренировка. Не забудь открыть бота!"
                )
            except:
                pass

        await asyncio.sleep(60)