
// Подключаемся к сеерверу чата
let chatServer = new WebSocket('ws://192.168.0.111:3030/')
let username = 'Admin'

let response = {
    username: username,
    address: 'Я живу у тебя дома',
    color: 'orange'
}
// Когда заходим на сайт отправляем наше первое сообщение серверу
chatServer.onopen = function (event) {
    // Отправляем первые данные серверу в JSON формате
    response.message = 'init'
    chatServer.send(JSON.stringify(response))
}

// Событие когда сервер нам присылает сообщение
chatServer.onmessage = function (event) {
    let chatMessageContainer = document.getElementsByClassName(
        'chat-message-container'
    )
    
    // Текущее время
    let time = `
        ${(new Date()).getHours()}
        :
        ${(new Date()).getMinutes()}
    `
    // Из сервера приходит в JSON формате
    // Мы его преобразуем в JS обьект (как dict python)
    let data = JSON.parse(event.data)
    let direction = ''
    if (
        data.username.toLowerCase()
        == response.username.toLowerCase()
    )
    {
        direction = 'text-md-end'
    }
    // Показываем получанное сообщение из сервера в div chat-message-parent
    chatMessageContainer[0].innerHTML += `
        <h2 class="text-md-end chat-message-parent">
            <div class="chat-author style="color:${data.color}">
                ${data.username}
            </div>
            <span class="chat-message">
                ${data.message}
                <i class="badge chat-message-time">${time}</i>
            </span>
        </h2>    
    `
    chatMessageContainer[0].scrollTop = chatMessageContainer[0].scrollHeight
}

// Событие работает когда сервер завершается 
chatServer.onclose = function () {
    console.log('Соеденение завершено')
}

// Кнопка ОТПРАВИТЬ
let sendMessageButton = document.getElementById(
    'chat-message-send-button'
)

function onClickSendButton() {
    // Получаем message inputs
    let messageInput = document.getElementById(
        'chat-message-input'
    )

    response.message = messageInput.value
    chatServer.send(JSON.stringify(response))

    
    // Выводим текст из message input в chat-message-container
    
    messageInput.value = ''
}

// Событие работает когда мы нажимаем на кнопка ОТПРАВИТЬ
sendMessageButton.addEventListener('click', onClickSendButton)