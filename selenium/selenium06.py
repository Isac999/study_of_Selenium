from time import sleep
from selenium.webdriver import Chrome

url = "https://selenium.dunossauro.live/aula_05_b.html"
driver = Chrome()
driver.get(url)

title_names = [] #lista de titulos
creation_dates = [] #lista de datas de criação
classes = driver.find_elements_by_class_name('linguagens') #buscando todos os elementos que tem a classe de 'linguagens'
n = 0
for item in classes: 
    title = classes[n].find_element_by_tag_name('h2').text #buscando o titulo
    title_names.append(title)
    dates = classes[n].find_element_by_tag_name('p').text #buscando a data de criação
    creation_dates.append(dates)
    n = n + 1
#fazendo um dicionário com chave e valor
chave_valor = {}
posicao = 0
for chave in title_names:
    chave_valor[chave] = creation_dates[posicao]
    posicao = posicao + 1