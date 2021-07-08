
import websockets
import asyncio
import json

# Здесь храним подключенных к серверу клиентов
users = set()

async def message(websocket, path):
    while True:
        # Получаем сообщение из клиента в формате JSON
        json_response = await websocket.recv()
        # Преобразуем JSON ответ в dict
        response_dict = json.loads(json_response)
        # Выводим сообщение клиента для дебагга
        print('Сообщение', response_dict['message'])

        # Проверяем если клиент вперные подключается
        if response_dict['message'] == 'init':
            # Когда пользователь первые подключается мы его запоминаемг users
            users.add(websocket)
            for user in users:
                    response_dict['message'] = 'вошел'

                    if user.closed == False:
                        # Отправляем клиенту JSON
                        await user.send(send_text)

        else: 
            # Заново отправляем сообщение всем
            for user in users:
                if user.closed == False:
                    await user.send(
                            response_dict['username']
                            + ':' +
                            response_dict['message']
                        )


# Создаем сервер веб чата на порту 3030
server = websockets.serve(message, port=3030)
print('Наш веб чат сервер запущен...')

# Запуск веб чата сервера
asyncio.get_event_loop().run_until_complete(server)
# Запуск сервера на постоянную основу
asyncio.get_event_loop().run_forever()