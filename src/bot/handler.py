from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from src.serializer.serializer import ConverterSerializer

router = Router()
converter = ConverterSerializer()


@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer("Привет! Я бот для конвертации валют. Используй /help для получения информации о командах.")


@router.message(Command("help"))
async def help_handler(msg: Message):
    await msg.answer('Доступные команды:\n'
                     '/start - начало работы\n'
                     '/help - список команд\n'
                     '/convert &lt;amount&gt; &lt;from_currency&gt; to &lt;to_currency&gt; - конвертация валюты\n')


@router.message(Command("convert"))
async def message_handler(msg: Message):
    convert_info = msg.text.split()[1:]
    result = converter.get_result(*convert_info)
    message = f"Результат конвертации из {convert_info[1]} в {convert_info[2]} равен {result}"
    await msg.answer(message)
