import asyncio
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from config import BOT_TOKEN
from database.db import init_db
from handlers import common, programs, exercises, stats
from utils.notifications import daily_notification


async def main():
    # Инициализация базы данных
    init_db()
    print("✅ База данных инициализирована")

    # Создаем бота и диспетчер
    bot = Bot(token=BOT_TOKEN)
    storage = MemoryStorage()
    dp = Dispatcher(storage=storage)

    # Регистрируем роутеры
    dp.include_router(common.router)
    dp.include_router(programs.router)
    dp.include_router(exercises.router)
    dp.include_router(stats.router)

    # Запускаем фоновую задачу уведомлений
    asyncio.create_task(daily_notification(bot))

    # Запускаем бота
    print("🚀 Бот запущен!")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())