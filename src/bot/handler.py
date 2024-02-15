from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()


@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer("Привет! Я бот для конвертации валют. Используй /help для получения информации о командах.")


@router.message()
async def message_handler(msg: Message):
    text = msg.text
    print(text)