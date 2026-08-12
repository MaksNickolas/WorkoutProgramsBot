import asyncio
import sys
from pathlib import Path

# Добавляем корневую папку в путь
sys.path.append(str(Path(__file__).parent))

from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from database.db import init_db
from handlers import common, programs, exercises, stats
from utils.notifications import daily_notification


async def main():
    # Инициализируем базу данных
    init_db()

    # Создаем бота и диспетчер
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    # Регистрируем роутеры
    dp.include_router(common.router)
    dp.include_router(programs.router)
    dp.include_router(exercises.router)
    dp.include_router(stats.router)

    # Запускаем фоновую задачу уведомлений
    asyncio.create_task(daily_notification(bot))

    # Запускаем бота
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())