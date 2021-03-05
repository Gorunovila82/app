
import telebot,requests

bot = telebot.TeleBot('1612428385:AAFNTgOosA50Lf_Q3QiukGAQPyoIQqNeyqo')

@bot.message_handler()
def help_message(message):
    bot.send_message(message.chat.id, requests.get("http://ip-api.com/json/").content)

bot.infinity_polling()