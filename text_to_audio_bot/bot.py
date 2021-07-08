
import telebot
import pyttsx3
import calendar
import time

bot = telebot.TeleBot('1890634532:AAGLTkRimW9CfrlvsjiRn9P-Va2BQXUhslY')


@bot.message_handler(content_types='text')
def get_message(message):
    message_splitted = message.text.lower().split('=')

    command = message_splitted[0].strip()
    text = message_splitted[1].strip()
    chat_id = message.chat.id

    if command == 'скажи':
        audio_engine = pyttsx3.init()
        # Создаем имя файла mp3 с помощью временной метки
        filename = str(calendar.timegm(time.gmtime())) + '.mp3'

        # Преобразуем текст в аулио
        # и отправляем в папку /home/neo/Downloads/*.mp3
        audio_engine.save_to_file(
            text,
            '/home/amantur/Загрузки/audios/' + filename
        )
        audio_engine.setProperty('rate', 20)
        # Запускаем аудио движка для сохранения
        audio_engine.runAndWait()

        # Отправляем
        bot.send_message(chat_id, 'Ваше аудио: ')
        audio_file = open('/home/amantur/Загрузки/audios/' + filename, 'rb')
        bot.send_audio(chat_id, audio_file)


print('Бот работает...')
bot.polling()