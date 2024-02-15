from openai import OpenAI

from src.settings.settings import SettingsManager


class CurrencyConverterAssistant:
    def __init__(self):
        self.__api_key = SettingsManager.get_chatgpt_token()
        self.model_name = "gpt-3.5-turbo-0613"
        self.assistant = OpenAI(api_key=self.__api_key)

    def generate_response(self, user_message):
        response = self.assistant.chat.completions.create(
            model=self.model_name,
            messages=[
                {
                    "role": "system",
                    "content": "You are a currency converter assistant. "
                               "You must answer to people for hello and goodbye "
                               "on russian language and talk with people",
                },
                {"role": "user", "content": user_message},
            ],
        )

        assistant_response = response["choices"][0]["message"]["content"]

        return assistant_response
