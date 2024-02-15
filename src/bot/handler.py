import logging

from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from src.api.chatgpt import CurrencyConverterAssistant
from src.serializer.serializer import ConverterSerializer
from src.utils.utils import filter_message


logger = logging.getLogger(__name__)
router = Router()
converter = ConverterSerializer()
assistant = None


@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer("Привет! Я бот для конвертации валют. Используй /help для получения информации о командах.")


@router.message(Command("help"))
async def help_handler(msg: Message):
    await msg.answer('Доступные команды:\n'
                     '/start - начало работы\n'
                     '/help - список команд\n'
                    '/assistant - подключить виртуального ассистента\n'
                    '/convert &lt;amount&gt; &lt;from_currency&gt; to &lt;to_currency&gt; - конвертация валюты\n')


@router.message(Command("assistant"))
async def assistant_handler(msg: Message):
    global assistant
    try:
        assistant = CurrencyConverterAssistant()
        await msg.answer("Ассистент успешно подключен! Наслаждайтесь!")
    except Exception as e:
        logger.error(f"Exception catched in route assistant {e}")
        await msg.answer("Что-то пошло не так. Обратитесь к этой функции позже.")


@router.message(Command("convert"))
async def message_handler(msg: Message):
    convert_info = msg.text.replace("to", "").split()[1:]
    logger.info(f"userId: {msg.from_user.id} Name:{msg.from_user.username} trying to convert {convert_info}")
    try:
        result = converter.get_result(*convert_info)
        message = f"Результат конвертации из {convert_info[1]} в {convert_info[2]} равен {result}"
        await msg.answer(message)
    except Exception as e:
        await msg.answer(str(e))
        logger.error(f"Incorrect data: {e}, {convert_info}")




@router.message()
async def messages_handler(msg: Message):
    global assistant
    if assistant:
        try:
            await msg.answer("Подождите, ассистент думает...")
            await msg.answer(assistant.generate_response(msg))
        except Exception as e:
            logger.error(f"Exception catched {e}")

            await msg.answer("Ассистент временно недоступен.")
            assistant = None

    if any(keyword in filter_message(msg.text) for keyword in ["привет", "hello"]):
        await msg.answer("И тебе привет, Мой дорогой друг!")

    if any(keyword in filter_message(msg.text) for keyword in ["пока", "goodbye"]):
        await msg.answer("И тебе пока, Мой дорогой друг!")
