import telebot
from gtts import gTTS
import os
bot = telebot.TeleBot(os.environ['TELEGRAMBOT_TOKEN'])
print(os.environ['TELEGRAMBOT_TOKEN'])
def text2mp3(s):
    try:
        tts = gTTS(s, lang='en', tld='com.au')
        tts.save(f'{s}.mp3')
        return None
    except Exception as e:
        return 'Cant convert to mp3'

@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Send to me something and I send back audio with your message.')

@bot.message_handler(commands=["remove"])
def start(m, res=False):
    path = os.environ['PROJECT_PATH']
    print(path)
    for file in os.listdir(path):
        if file.endswith('.mp3'):
            os.remove(path+file)

@bot.message_handler(content_types=["text"])
def handle_text(message):
    text2mp3(message.text)
    path = os.environ['PROJECT_PATH']
    bot.send_audio( message.chat.id,
                    audio=open(f'{path}{message.text}.mp3','rb') )

# Запускаем бота
bot.polling(none_stop=True, interval=0)
