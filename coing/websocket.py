import json
import os
import sys
import logging
import asyncio
import websockets

from websockets.sync.client import connect
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from core.const import API_UPBIT_WS_URL

async def ws_client():
    
    test = [
            {"ticket":"test"},
            {"type":"ticker", "codes":["KRW-BTC"]},
            {"format":"SIMPLE"}
        ]
    
    data = json.dumps(test)
        
    async with websockets.connect(API_UPBIT_WS_URL) as websocket:
        await websocket.send(data)
        
        while True:
            res = await websocket.recv()
            res_json = json.loads(res)  
            print(res_json)
    
async def main():
    await ws_client()
        
if __name__ == "__main__":
    asyncio.run(main()) 
    
def test():
    print(API_UPBIT_WS_URL)