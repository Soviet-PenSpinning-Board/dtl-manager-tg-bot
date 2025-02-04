import aiogram

from dtl_manager_tg_bot.config import getenv

from .routing import dp


async def start() -> None:
    bot = aiogram.Bot(token=getenv("token"))
    await dp.start_polling(bot)
