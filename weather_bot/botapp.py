import telebot
import requests
import pytube
import calendar
import time

bot = telebot.TeleBot('1878049375:AAGTcVzkfozMyEz66ibQF3EWnJpwkejZwUY')

weather_url = 'https://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid=fa0c69065a227aae0ae1081d5953bcfa&units=metric'


# начала разговора с ботом
@bot.message_handler(commands=['start', 'старт'])
def welcome(message):
    msg = ' Я бот, Привет как дела'
    bot.reply_to(message, msg)


@bot.message_handler(content_types='text')
def get_message(message):
    if message.text.lower() == 'привет':
        print(message.from_user)
        print('Клиент пишет', message.text)
        bot.send_message(message.from_user.id, 'Привет')
    elif message.text.split(' ')[0] == 'погода':
        textsplitted = message.text.lower().split(' ')
        city = textsplitted[2]
        country = textsplitted[1]
        # окончательный URL для запроса прогноза погоды
        w_final_url = weather_url.format(
            city = city,
            country = country
        )
        response = requests.get(w_final_url)
        weather_dict = response.json()
        msg = 'Погода в {city} {temp} градусов.'.format(
            city = city,
            temp = weather_dict['main']['temp']
        )
        bot.send_message(message.from_user.id, msg)
    elif message.text.find('youtube.com/watch?v='):

        #  получаем ссылку youtube
        url = message.text

        youtube = pytube.YouTube(url)

        # выбираем разрешение для скачивание видео
        video = youtube.streams.get_by_resolution('360p')

        # отправляем клиенту сообщение чтобы не волновался
        bot.send_message(message.chat.id, 'мы качаем видео подождите...')
        # название файла как временная метка
        filename = str(calendar.timegm(time.gmtime()))

        # качаем видео и помещаем в папку videos
        video.download(
            filename = filename,
            output_path = '/home/neo/Downloads/videos'
        )

        # оповещаем клиента что скачали видео и говорим ему отправляем
        bot.send_message(message.chat.id, 'мы скачали ваше видео вот держите')
        # полный путь файлу
        filepath = '/home/neo/Downloads/videos/{filename}.{ext}'.format(
            filename = filename,
            ext = 'mp4'
        )
        # открываем видео из папки читаем и готовим для отправки
        downloaded_video = open(filepath, 'rb')

        # отправляем видео клиенту потоком
        bot.send_video(message.chat.id, downloaded_video)

print('Бот работает..')
# запускаем бота
bot.polling()