from src.api.converter import ConverterAPI


class JsonSerializer:
    @staticmethod
    def json_to_result_of_conversion(data: dict):
        return str(data.get("conversion_result"))


class ConverterSerializer:
    def __init__(self):
        self.conversion_api = ConverterAPI()

    def get_result(self, amount, base_cur, new_cur):
        result = self.conversion_api.convert(amount, base_cur, new_cur)
        if result.get("result") == "error":
            raise TypeError("Вы неправильно ввели данные. Проверьте правильность написания входных данных.")
        return JsonSerializer.json_to_result_of_conversion(result)
