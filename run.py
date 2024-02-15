import os
import logging
import asyncio

from src.bot.main import run_bot

project_dir = os.path.dirname(os.path.abspath(__file__))
log_file_path = os.path.join(project_dir, "bot_logs.log")
logging.basicConfig(filename=log_file_path, level=logging.INFO)
logger = logging.getLogger(__name__)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(run_bot())
