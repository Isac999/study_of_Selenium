from selenium import webdriver
from time import sleep

url = 'http://selenium.dunossauro.live/aula_04_a.html'
driver = webdriver.Chrome()
driver.get(url)

sleep(10)

#como eu resolvi sem ver o video:
"""
lista_n_ordenada01 = driver.find_element_by_tag_name('ul') #pegar apenas o primeiro elemento de <ul>, que seria (DuckDuckGo/Google). Se usassemos o 'elements' no lugar de apenas um elemento, ele nos retornaria uma lista com dois elementos (Duck/Google e Item1/Item2) 
elemento01 = lista_n_ordenada01.find_elements_by_tag_name('li') #atravéz da nossa variavel 'lista_n_ordenada01', pedimos para o selenium gerar outra lista com o conteúdo de <li> ('Google' e 'DuckGo'), e armazenar no nosso 'elemento01' 
print(f'Conteúdo da tag <li> 01 = {elemento01[0].text}')
print(f'Conteúdo da tag <li> 02 = {elemento01[1].text}')

lista_n_ordenada02 = driver.find_elements_by_tag_name('ul') #essa nova lista contém todos os conteúdos de <ul>, pois usamos o 'elements' (que pega todos os valores de <ul> no script HTML)
elemento02 = lista_n_ordenada02[1].find_elements_by_tag_name('li') #aqui, pedimos para ele pegar apenas o último (que seria o segundo) elemento de <ul> (contendo Item1/Item2, juntos) e especificamos isso no 'lista_n_ordenada[1]'. Após isto pedimos para ele criar uma lista com o conteúdo dos <li> (Item1 e Item2, respectivamente separados)
print(f'Conteúdo da tag <li> 03 = {elemento02[0].text}')
print(f'Conteúdo da tag <li> 04 = {elemento02[1].text}')
"""

#forma alternativa e usando menos linhas(que eu resolvi tbm sem ver o video rsrs):
lista_n_ordenada = driver.find_elements_by_tag_name('ul')

elemento01 = lista_n_ordenada[0].find_elements_by_tag_name('li')
print(f'Conteúdo da tag <li> 01 = {elemento01[0].text}')
print(f'Conteúdo da tag <li> 02 = {elemento01[1].text}')

elemento02 = lista_n_ordenada[1].find_elements_by_tag_name('li')
print(f'Conteúdo da tag <li> 03 = {elemento02[0].text}')
print(f'Conteúdo da tag <li> 04 = {elemento02[1].text}')


driver.quit()