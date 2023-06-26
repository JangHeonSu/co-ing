from django.test import TestCase

import requests

url = "https://api.upbit.com/v1/market/all"

resp = requests.get(url)
data = resp.json()


for coin in data:
    ticker = coin['market']
    print(ticker)