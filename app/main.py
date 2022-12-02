import telebot
import requests
from bs4 import BeautifulSoup

bot = telebot.TeleBot('5607061999:AAHJMd0sdmwHf7VumXkoMEt1vfXQS4JkUpQ')

# парсинг сайта с погодой
def get_data(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    data = soup.find('span', {'class': 'value colorize-server-side'}).text[:-1]
    return data


# генерация кнопочного меню в чате
@bot.message_handler(commands=['start'])
def start(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    key_moscow = telebot.types.KeyboardButton(text='Москва')
    key_saint = telebot.types.KeyboardButton(text='Питер')
    key_other = telebot.types.KeyboardButton(text='Другой')
    keyboard.add(key_moscow, key_saint, key_other)
    bot.send_message(message.chat.id, text='Привет! Выбери город из списка', reply_markup=keyboard)


# обработка введенных пользователем данных
@bot.message_handler(content_types=['text'])
def func(message):
    if message.text == "Москва":
        bot.send_message(message.chat.id, text=get_advice('https://www.meteoservice.ru/weather/overview/moskva'))
    elif message.text == "Питер":
        bot.send_message(message.chat.id, text=get_advice('https://www.meteoservice.ru/weather/overview/sankt-peterburg'))
    elif message.text == "Другой":
        bot.send_message(message.chat.id, text='Извини. Пока мало компетенций для совета по другим городам :(')
    else:
        bot.send_message(message.chat.id, text="Не понял тебя. Выбери город из меню и все будет чики-пуки")
bot.polling(none_stop=True)




