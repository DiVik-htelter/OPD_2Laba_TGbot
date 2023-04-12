import telebot
from bs4 import BeautifulSoup # импортируем библиотеку BeautifulSoup
import requests # импортируем библиотеку requests

def parser_farmakopeika(name):
    url = 'https://farmakopeika.ru/search?query=' + name # передаем необходимы URL адрес
    page = requests.get(url) # отправляем запрос методом Get на данный адрес и получаем ответ в переменную
    #print(page.status_code) # смотрим ответ
    soup = BeautifulSoup(page.text, "html.parser") # передаем страницу в bs4

    block = soup.findAll('div',id="products-app") # находим  контейнер с нужным классом
    description = ''
    for data in block: # проходим циклом по содержимому контейнера
        if data.find('div'): # находим тег
            description = data.text # записываем в переменную содержание тега    
    description = description.replace('В корзину','')
    for i in range(4):
        description = description.replace('\n\n','\n')
    description = description.replace('\nнет',' нет')
    description = description.replace('\nесть',' есть')
    description = description.replace('В аптеках:\n','В аптеках: ')
    description = description.replace('от','Цена от: ')
    description = description.replace('\n\n','\n')
    count = 1
    for i in description:
        if i == '\n':
            count+=1
      # if count == 4:
      #     description[i]
    s = '_'
    print(name,'\n',description,s*30)
    if description == '':
      return 'Ничего не нашлось'
    return description

token='TOKEN'
bot=telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
	bot.send_message(message.chat.id,'Привет, я пока что не полноценный, но уже могу находить лекарства в фармакопейке, просто введи название того, что тебе нужно!')


@bot.message_handler(content_types=['text'])
def echo_message(message):
  bot.send_message(message.chat.id,text=f"{parser_farmakopeika(message.text)}")
bot.infinity_polling()



def parser_apteka(name):
    url = 'https://apteka.ru/search/?q=' + name # передаем необходимы URL адрес
    page = requests.get(url) # отправляем запрос методом Get на данный адрес и получаем ответ в переменную
    #print(page.status_code) # смотрим ответ
    soup = BeautifulSoup(page.text, "html.parser") # передаем страницу в bs4

    block = soup.findAll('div',class_="cards-list-sort-filter") # находим  контейнер с нужным классом
    description = ''
    for data in block: # проходим циклом по содержимому контейнера
        if data.find('a'): # находим тег
            description = data.text # записываем в переменную содержание тега

   # print(description)
