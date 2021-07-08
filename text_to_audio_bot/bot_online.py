
import telebot
import gtts
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
        # Создем имя файла mp3 с помощью временной метки
        filename = str(calendar.timegm(time.gmtime())) + 'mp3'

        audio = gtts.gTTS(text, lang='ru')
        audio.save('/home/amantur/Загрузки/audios/' + filename)

        bot.send_message(chat_id, 'Ваше аудио готова')
        bot.send_message(chat_id, 'Сейчас отправлю')

        audio_file = open('/home/amantur/Загрузки/audios/' + filename, 'rb')
        bot.send_audio(chat_id, audio_file)

    elif command == 'tell':
        # Создем имя файла mp3 с помощью временной метки
        filename = str(calendar.timegm(time.gmtime())) + 'mp3'

        audio = gtts.gTTS(text, lang='en')
        audio.save('/home/amantur/Загрузки/audios/' + filename)

        bot.send_message(chat_id, 'Ваше аудио готова')
        bot.send_message(chat_id, 'Сейчас отправлю')

        audio_file = open('/home/amantur/Загрузки/audios/' + filename, 'rb')
        bot.send_audio(chat_id, audio_file)


    elif command == 'sagen':
        # Создем имя файла mp3 с помощью временной метки
        filename = str(calendar.timegm(time.gmtime())) + 'mp3'

        audio = gtts.gTTS(text, lang='de')
        audio.save('/home/amantur/Загрузки/audios/' + filename)

        bot.send_message(chat_id, 'Ваше аудио готова')
        bot.send_message(chat_id, 'Сейчас отправлю')

        audio_file = open('/home/amantur/Загрузки/audios/' + filename, 'rb')
        bot.send_audio(chat_id, audio_file)


print('Бот работает...')
bot.polling()