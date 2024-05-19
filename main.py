import asyncio
from aiogram import Bot, Dispatcher
from psix import dp, bot
async def main():
    await dp.start_polling(bot)
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(dp.start_polling())
    loop.run_forever()