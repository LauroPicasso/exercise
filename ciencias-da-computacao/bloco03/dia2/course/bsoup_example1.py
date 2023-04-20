import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com"
page = requests.get(url)
html_content = page.text

# Cria uma instância do objeto Beautiful Soup e usa o parser de HTML nativo
# do Python
soup = BeautifulSoup(html_content, "html.parser")

# Utiliza o método prettify para melhorar a visualização do conteúdo
# print(soup.prettify())

# acessando a tag 'title'
title = soup.title

# retorna o elemento HTML da tag
print(title)
# <title>Quotes to Scrape</title>

# o tipo de 'title' é tag
print(type(title))
# <class 'bs4.element.Tag'>

# o nome de 'title' é title
print(title.name)
# title

# acessando a tag 'footer'
footer = soup.footer

# acessando o atributo classe da tag footer
print(footer['class'])
# ['footer']

# retorna o elemento HTML da tag
print(title)
# <title>Quotes to Scrape</title>

# Acessando a string de uma tag
print(title.string)
# Quotes to Scrape

# Verificando o tipo dessa string
print(type(title.string))
# <class 'bs4.element.NavigableString'>
