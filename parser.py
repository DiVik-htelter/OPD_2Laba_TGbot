from bs4 import BeautifulSoup # импортируем библиотеку BeautifulSoup
import requests # импортируем библиотеку requests





def farmakopeika(name):
    url = 'https://farmakopeika.ru/search?query=' + name # передаем необходимы URL адрес
    page = requests.get(url) # отправляем запрос методом Get на данный адрес и получаем ответ в переменную
    #print(page.status_code) # смотрим ответ
    soup = BeautifulSoup(page.text, "html.parser") # передаем страницу в bs4

    block = soup.findAll('div',id="products-app") # находим  контейнер с нужным классом
    description = ''
    for data in block: # проходим циклом по содержимому контейнера
        if data.find('div'): # находим тег
            description = data.text # записываем в переменную содержание тега    
    
    
    return sFarm(description)

def sFarm(s):
    s = s.replace('В корзину','')
    for i in range(4):
        s = s.replace('\n\n','\n')
    s = s.replace('\nнет',' нет')
    s = s.replace('\nесть',' есть')
    s = s.replace('В аптеках:\n','В аптеках: ')
    s = s.replace('от','Цена от: ')
    s = s.replace('\n\n','\n')

    rs =s.split(sep = '\n')

    for i in range(len(rs)):
        if i%4==0:
            rs[i]+='\n'
    s = "\n".join(rs)
    
    print('\n',s,'-'*35)
    if s == '':
        return 'Ничего не нашлось'
    return s

'''

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
'''