
from requests import get
from pprint import PrettyPrinter
import os
from dotenv import load_dotenv


load_dotenv()
API_KEY = os.getenv("API_KEY")
BASE_URL = "https://api.freecurrencyapi.com/v1/currencies"

printer = PrettyPrinter()

def getCurrencies():
    url = f"{BASE_URL}?apikey={API_KEY}"
    data = get(url).json()
    printer.pprint(data)


getCurrencies()