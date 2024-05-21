import telebot
import json
import requests
from config import keys



class APIException(Exception):
    pass
class MoneyConverter:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):
        if quote == base:
            raise APIException(f'Невозможно перевести одинаковые валюты {base}')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {quote}')
        try:
            base_ticker = keys[base]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {base}')
        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Не удалось обработать количество {amount}')

        r = requests.get(
            f'https://v6.exchangerate-api.com/v6/7972d1ecf1f6627c6113862e/pair/{quote_ticker}/{base_ticker}')
        total_base = json.loads(r.content)['conversion_rate']

        return total_base * amount