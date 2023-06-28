import json
import os
import sys
import logging
import asyncio
import websockets

from websockets.sync.client import connect
# from core import upbit
# from core.const import API_UPBIT_WS_URL

async def websocket_test():
    
    test = [
            {"ticket":"test"},
            {"type":"ticker", "codes":["KRW-BTC"]},
            {"format":"SIMPLE"}
        ]
    
    data = json.dumps(test)
        
    async with websockets.connect('wss://api.upbit.com/websocket/v1') as websocket:
        await websocket.send(data)
        
        while True:
            res = await websocket.recv()
            res_json = json.loads(res)  
            print(res_json)
    
async def main():
    await websocket_test()
        
if __name__ == "__main__":
    asyncio.run(main()) 