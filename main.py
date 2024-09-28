import telebot
from telebot import types
from config import TOKEN

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    
    # Кнопка для открытия Web App
    web_app_info = types.WebAppInfo("https://your-web-app-url.com")  # Замените на URL вашего веб-приложения
    web_app_btn = types.KeyboardButton(text="Открыть Web App", web_app=web_app_info)
    
    markup.add(web_app_btn)
    bot.send_message(message.chat.id, "Нажмите кнопку ниже, чтобы открыть Web App.", reply_markup=markup)

bot.polling(non_stop=True)