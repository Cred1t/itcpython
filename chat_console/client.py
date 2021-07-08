
import asyncio
import websockets


server_url = 'ws://192.168.0.111:3030'
username = 'Erlan'


async def client_message():
    # Подключаемся к серверу 
    async with websockets.connect(server_url) as websocket:
        # Мы когда первый раз подключаемся отправляем сообщение init чтобы сказать сереверу что первый раз подключаемся
        await websocket.send('init:'+username)
        # Создаем бесконечный цикл непрерывной отправки сообщений 
        while True:
            message = input('Введите сообшение: ')

            # Отключаем клиент когда мы пишем exit
            if message == 'exit' or websocket.closed == True:
                # Завершаем соедение с сервером
                # await websocket.close()
                print('Программа завершена')
                break

            await websocket.send(username+'>>>'+message)
            print('Сообщение отправлено')


# Запуск сервера
asyncio.get_event_loop().run_until_complete(client_message())