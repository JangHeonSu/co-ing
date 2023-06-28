import jwt
import json
import hashlib
import requests
import uuid
from core.const import API_ACCESS_KEY, API_SECRET_KEY, API_UPBIT_SERVER_URL

params = {
  'currency': 'KRW',
  'state': 'done'
}
query_string = json.dumps(params)

m = hashlib.sha512()
m.update(query_string.encode("utf-8"))
query_hash = m.hexdigest()

payload = {
    'access_key': API_ACCESS_KEY,
    'nonce': str(uuid.uuid4()),
}

jwt_token = jwt.encode(payload, API_SECRET_KEY)
authorization = 'Bearer {}'.format(jwt_token)
headers = {
  'Authorization': authorization,
  'Content-Type': 'application/json'
}

res = requests.get(API_UPBIT_SERVER_URL["ACCOUNTS"], headers=headers)
print(res.json())