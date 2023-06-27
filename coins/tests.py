from django.test import TestCase

import jwt
import hashlib
import requests
import uuid
from urllib.parse import urlencode, unquote
from core.const import API_ACCESS_KEY, API_SECRET_KEY, API_UPBIT_SERVER_URL


print(API_ACCESS_KEY)
print(API_SECRET_KEY)
print(API_UPBIT_SERVER_URL)

params = {
  'currency': 'KRW',
  'state': 'done'
}
query_string = unquote(urlencode(params, doseq=True)).encode("utf-8")

m = hashlib.sha512()
m.update(query_string)
query_hash = m.hexdigest()

payload = {
    'access_key': API_ACCESS_KEY,
    'nonce': str(uuid.uuid4()),
}

jwt_token = jwt.encode(payload, API_SECRET_KEY)
authorization = 'Bearer {}'.format(jwt_token)
print(authorization)
headers = {
  'Authorization': authorization,
}

res = requests.get(API_UPBIT_SERVER_URL + "/v1/account", headers=headers)
print(res.json())
# print(f"{currency_data['currency']} : {currency_data['balance']}")

