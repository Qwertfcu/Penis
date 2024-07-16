import telebot
from MukeshAPI import api

# Вставьте ваш токен здесь
TOKEN = '7416094146:AAGNbHXRELgfMtQ_ZH5v6uA3fsPt7ihikbA'

# Создаем экземпляр бота
bot = telebot.TeleBot(TOKEN)

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я ваш негр.")

# Обработчик команды /help
@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "Напишите /start для начала.")

@bot.message_handler(commands=['sendphoto'])
def send_photo(message):
    image=api.ai_image(message.text)
    bot.send_photo(message.chat.id,image)

# Обработчик всех остальных сообщений
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message,message.text)


# Запуск бота
bot.polling()

if __name__ == '__main__':
    bot.infinity_polling()