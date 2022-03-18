#1 - pegar o link das aulas e colocar na lista
#2 - clickar no exercício 3

from selenium import webdriver
from time import sleep

url = 'http://selenium.dunossauro.live/aula_04.html'
driver = webdriver.Chrome()
driver.get(url)

sleep(5)

####Colocando todos os links das aulas em uma lista:
aside = driver.find_element_by_tag_name('aside') #localizando a 'Lista de Aulas' atravéz da tag <aside>
tag_a01 = aside.find_elements_by_tag_name('a') #criando uma lista com todas as tags <a>
minha_lista_de_aulas = [] #minha lista com os links
contador = 0
for b in range(0,7):
    links = tag_a01[contador].get_attribute('href') #pegando o link das aulas pelo atributo de 'href', em suas respectivas posições
    print(links) 
    minha_lista_de_aulas.append(links) #adicionando cada link na lista de links
    contador = contador + 1

####Clicando no exercício 3:
main = driver.find_element_by_tag_name('main') #localizando a 'Lista de Exercícios' atravéz da tag <main>
tag_a02 = main.find_elements_by_tag_name('a') #criando uma lista com todas as tags <a>
print(tag_a02[2].text) 
tag_a02[2].click() #clicando na tag <a> e especificando sua posição na lista ([2])