import os

API_ACCESS_KEY = os.environ.get('UPBIT_OPEN_API_ACCESS_KEY')
API_SECRET_KEY = os.environ.get('UPBIT_OPEN_API_SECRET_KEY')
API_UPBIT_SERVER_URL = {
    "ACCOUNTS": "https://api.upbit.com/v1/accounts",
    "ORDER": "https://api.upbit.com/v1/order",
    "ORDERS": "https://api.upbit.com/v1/orders",
    "ORDERS_CHANCE": "https://api.upbit.com/v1/orders/chance",
    "WALLET": "https://api.upbit.com/v1/wallet",
    "MARKET": "https://api.upbit.com/v1/market/all?isDetails=false",
    "TICKER": "https://api.upbit.com/v1/ticker",
}

API_UPBIT_WS_URL = 'wss://api.upbit.com/websocket/v1'
