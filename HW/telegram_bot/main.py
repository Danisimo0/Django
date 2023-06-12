import requests
from bs4 import BeautifulSoup
from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

def get_bitcoin_price():
    url = 'https://coinmarketcap.com/currencies/bitcoin/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    price = soup.find('span', class_='cmc-details-panel-price__price').text
    return price

def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Привет! Я бот для парсинга криптовалют. Введите /
