import telebot

import parser
import TOKEN



bot=telebot.TeleBot(TOKEN.TOKEN)

sHallo = 'Привет, я пока что не полноценный, но уже могу находить лекарства в фармакопейке, просто введи название того, что тебе нужно!'

@bot.message_handler(commands=['start'])
def start_message(message):
	bot.send_message(message.chat.id,sHallo)


@bot.message_handler(content_types=['text'])
def echo_message(message):
  bot.send_message(message.chat.id,text=f"{parser.farmakopeika(message.text)}")
bot.infinity_polling()
'''
parser.farmakopeika("цитрамон")
s = input()
'''