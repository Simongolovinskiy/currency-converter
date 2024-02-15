import requests
from src.settings.settings import SettingsManager


class ConverterAPI:
    def __init__(self):
        self.__api_key = SettingsManager.get_converter_api_key()
        self.base_url = SettingsManager.get_converter_url()

    def convert(self, amount, base_cur, new_cur):

        response = requests.get(
            f"{self.base_url}/{self.__api_key}/pair/{base_cur}/{new_cur}/{amount}"
        )
        return response.json()
