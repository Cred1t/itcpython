
import asyncio
import websockets

server_url = 'ws://192.168.0.111:3030'
username = 'Pingvin'


async def client_message():
    # Подключаемся к серверу асинхронный код
    async with websockets.connect(server_url) as websocket:
        await websocket.send('init:' + username)
        while True:
            message = await websocket.recv()
            print(message)


# Запуска клиента консоль чата
asyncio.get_event_loop().run_until_complete(client_message())