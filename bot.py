from telebot import TeleBot, types
from dotenv import load_dotenv
import os

load_dotenv()

BOT_TOKEN = os.environ.get("BOT_TOKEN")
WEBAPP_URL = os.environ.get("WEBAPP_URL")

bot = TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    webApp = types.WebAppInfo(WEBAPP_URL)
    markup.add(types.KeyboardButton("Open MiniApp", web_app=webApp))
    bot.send_message(message.chat.id, "Open the mini app:", reply_markup=markup)

def send_message(chat_id, text):
    bot.send_message(chat_id, text)
