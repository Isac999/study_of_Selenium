from time import sleep
from selenium import webdriver

url = "https://selenium.dunossauro.live/aula_05_a.html"
driver = webdriver.Chrome()
driver.get(url)

creation_dates = [] #lista de datas de criação
name_id = ['python','haskell','lisp','prolog'] #lista com o nome dos id's
for item in name_id: #percorrendo cada elemento da lista de id's
    path01 = driver.find_element_by_id(item) #pegando os itens pelo seu respectivo id
    path02 = path01.find_element_by_tag_name('p').text #a partir do id pegamos o conteúdo do elemtento <p> (data de criação da linguagem)
    creation_dates.append(path02) #adicionando os dados a lista de data de criação
