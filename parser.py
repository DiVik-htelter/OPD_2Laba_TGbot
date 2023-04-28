from bs4 import BeautifulSoup # импортируем библиотеку BeautifulSoup
import requests # импортируем библиотеку requests

OnlyPrescription = 'Только по рецепту' 
Apteka = 'В аптеках:'

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

    s =s.split(sep = '\n')

    for i in range(len(s)-1):
        if s[i] == OnlyPrescription:
            s[i] = '\n'+s[i]
        
        elif Apteka in s[i]:
            s[i+1] = '\n' + s[i+1]
        
        

    s = "\n".join(s)
    
    print('\n',s,'-'*35)
    if s == '':
        return 'Ничего не нашлось'
    return s
