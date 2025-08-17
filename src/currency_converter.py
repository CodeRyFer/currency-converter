
from requests import get
from pprint import PrettyPrinter
import os
from dotenv import load_dotenv


load_dotenv()
API_KEY_1 = os.getenv("API_KEY_1")
API_KEY_2 = os.getenv("API_KEY_2")
BASE_URL = "https://api.freecurrencyapi.com/v1/currencies"

printer = PrettyPrinter()

def get_currencies():
    url = f"{BASE_URL}?apikey={API_KEY_1}"
    data = get(url).json()['data']

    data = list(data.items())

    data.sort()

    return data

def print_currencies(currencies):
    for _id, currency in currencies:
        name = currency.get('name', '')
        symbol = currency.get('symbol', '')
        print(f"{_id} - {name} - {symbol}")

def exchange_rate(currency1, currency2):
    getConversion = f"https://v6.exchangerate-api.com/v6/{API_KEY_2}/pair/{currency1}/{currency2}"
    data = get(getConversion).json()

    if len(data) == 0:
        print('Invalid currencies')
        return
    
    rate = list(data.values())[9]
    print(f"{currency1} -> {currency2} = {rate}")

    return rate
    
def convert(currency1, currency2, amount):
    rate = exchange_rate(currency1, currency2)
    if rate is None:
        return
    
    try: amount = float(amount)
    except:
        print("Invalid amount")
        return
    
    converted_amount = rate * amount
    print(f"{amount} {currency1} is equal to = {converted_amount} {currency2}")
    return converted_amount


#data = get_currencies()
#printer.pprint(data)
#print_currencies(data)

convert("USD", "CAD", 30)
