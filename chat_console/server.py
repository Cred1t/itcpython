
import websockets 
import asyncio

users = set()


async def on_message(websocket, path):
    message = ''
    while True:
        message = await websocket.recv()
        if websocket.find('init:') == 0:
            msq_sql = message.split(':')
            print(msq_sql[1], 'присоеденился')
            users.add({
                'user_name': msq_sql[1],
                'client_socket': websocket
            })
            for user in users:
                if user['client_scket'].closed == False:
                    user['client_socket'].send(
                        msg_spl[1]+'>>присоединился'
                    )
        else:
            print('->', message)

        print('-->', message)
        for user in users:
            if user['client_socket'].closed == False:
                await user['client_socket'].send(message)


# Создаем сервер веб чата на порту 3030
server =  websockets.serve(on_message, port=3030)
print('Наш веб чат сервер запущен...')

# Запуск веб чата сервера
asyncio.get_event_loop().run_until_complete(server)
# Запуск сервера на постоянную основу 
asyncio.get_event_loop().run_forever()