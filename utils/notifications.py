import asyncio
from datetime import datetime
from aiogram import Bot
from database.db import get_last_notification, update_last_notification


async def daily_notification(bot: Bot):
    """Отправляет уведомления в 8:00"""
    while True:
        now = datetime.now()

        if now.hour == 8 and now.minute == 0:
            # Здесь нужно получить список всех пользователей
            # Для простоты пока оставим заглушку
            # Позже можно добавить таблицу subscribed_users

            # Пример отправки админу
            try:
                await bot.send_message(
                    chat_id=ADMIN_ID,  # Добавь ADMIN_ID в config
                    text="🌅 Доброе утро! Сегодня у тебя тренировка. Не забудь открыть бота!"
                )
            except:
                pass

        await asyncio.sleep(60)