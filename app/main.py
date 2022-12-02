import telebot
import requests
from bs4 import BeautifulSoup

bot = telebot.TeleBot('5607061999:AAHJMd0sdmwHf7VumXkoMEt1vfXQS4JkUpQ')

# генерация кнопочного меню в чате
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, text='Привет! Выбери город из списка', reply_markup=keyboard)


bot.polling(none_stop=True)




