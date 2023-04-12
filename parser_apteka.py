#Задание: Нужно напарсить сайты аптек типа фармакопейти и т.д. по лекарствам.
#Что бы пользователь вводил название лекарства и кему выдавало то где его можно найти, цену количество в пачке и т.д.

from bs4 import BeautifulSoup # импортируем библиотеку BeautifulSoup
import requests # импортируем библиотеку requests
from fake_useragent import UserAgent

UserAgent().chrome
Out: 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2224.3 Safari/537.36'




'''
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
    for i in range(4):
        description = description.replace('\n\n','\n')
    print(description)



def parser_apteka(name): #Почему не парсится???
    url = 'https://apteka.ru/search/?q=' + name # передаем необходимы URL адрес
    page = requests.get(url) # отправляем запрос методом Get на данный адрес и получаем ответ в переменную
    print(page.status_code) # смотрим ответ
    soup = BeautifulSoup(page.text, "html.parser") # передаем страницу в bs4

    block = soup.findAll('div',class_="ViewSearch") # находим  контейнер с нужным классом
    description = ''
    for data in block: # проходим циклом по содержимому контейнера
        if data.find('span'): # находим тег
            description = data.text # записываем в переменную содержание тега
    #return description
    print(description)

'''




def parser_zdravcity(name):  # не парсится, код 403
    url = 'https://zdravcity.ru/search/?what=' + name
    page = requests.get(url, headers ={'User-Agent':UserAgent().chrome}) # отправляем запрос методом Get на данный адрес и получаем ответ в переменную
    #for key, value in page.request.headers.items():
     #   print(key+": "+value)
    print(page.status_code) # смотрим ответ
    soup = BeautifulSoup(page.text, "html.parser") # передаем страницу в bs4

    block = soup.findAll('div',class_="sc-58d8feb4-5 gWNFwp") # находим  контейнер с нужным классом
    description = ''
    for data in block: # проходим циклом по содержимому контейнера
        if data.find('div'): # находим тег
            description = data.text # записываем в переменную содержание тега
    #return description
    print(description)


while(True):
    name = input("введите лекарство для поиска в : ")

    parser_zdravcity('цитрамон')
