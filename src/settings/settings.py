import os

from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, "../.env"))


class SettingsManager:
    @staticmethod
    def get_converter_api_key():
        return os.getenv("converter_api_key")

    @staticmethod
    def get_converter_url():
        return os.getenv("base_url")

    @staticmethod
    def get_telegram_token():
        return os.getenv("telegram_token")
