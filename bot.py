from aiogram import Bot, Dispatcher, executor, types
import asyncio
from requests import get, post
import logging
import config

bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)


@dp.message_handler(content_types=['text'])
async def said(message: types.Message):
    await bot.send_message(message.chat.id, message.text)


if __name__ == '__main__':
    # dp.loop.create_task(get_start())
    executor.start_polling(dp, skip_updates=True)
