
from requests import get
from pprint import PrettyPrinter
import os
from dotenv import load_dotenv


load_dotenv()
API_KEY = os.getenv("API_KEY")
BASE_URL = "https://api.freecurrencyapi.com/v1/currencies"

printer = PrettyPrinter()

def get_currencies():
    url = f"{BASE_URL}?apikey={API_KEY}"
    data = get(url).json()['data']

    data = list(data.items())

    data.sort()

    return data

def print_currencies(currencies):
    for _id, currency in currencies:
        name = currency.get('name', '')
        symbol = currency.get('symbol', '')
        print(f"{_id} - {name} - {symbol}")


data = get_currencies()
#printer.pprint(data)
print_currencies(data)