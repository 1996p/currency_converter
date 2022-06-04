from enum import Enum
from bs4 import BeautifulSoup
import requests
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'currency_converter.settings')
import django
django.setup()
from mainapp.models import CurrencyPair
from .exceptions import *


API_KEY = 'f85b775347f74afcbde40b5d06e70e5e'
REQUEST_TEMPLATE = 'https://currate.ru/api/?get=rates&pairs={from_currency}{to_currency}&key={api_key}'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.119 YaBrowser/22.3.0.2435 Yowser/2.5 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
}


class Currency(Enum):
    USD = "Доллар США"
    RUB = "Российский Рубль"
    TRY = "Турецкая лира"
    EUR = "Евро"
    CHF = "Швейцарский фран"
    GBP = "Фунт стерлингов"
    JPY = "Японская йена"
    UAH = "Гривна"
    KZT = "Казахстанский тенге"
    BYN = "Белорусский рубль"
    CNY = "Китайский юань"
    PLN = "Польский злотый"


def get_pair_json(from_currency: Currency, to_currency: Currency) -> None:
    request = requests.get(url=REQUEST_TEMPLATE.format(from_currency=from_currency.name,
                                                       to_currency=to_currency.name,
                                                       api_key=API_KEY),
                           headers=HEADERS)
    if request.json()['status'] != 200:
        raise CantGetCurrencyData()

    price = parse_pair(data=request.json(), from_currency=from_currency, to_currency=to_currency)

    update_pair(from_currency=from_currency, to_currency=to_currency, price=price)


def parse_pair(data: dict, from_currency: Currency, to_currency: Currency) -> float:
    return float(data['data'][f'{from_currency.name}{to_currency.name}'])


def update_pair(from_currency: Currency, to_currency: Currency, price: float) -> None:

    pair = CurrencyPair.objects.get(first_currency_name=from_currency.name,
                                second_currency_name=to_currency.name)
    pair.price = price
    pair.save()


def main_func():
    pass


if __name__ == '__main__':
    main_func()
