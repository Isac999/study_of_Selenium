from selenium import webdriver
from time import sleep

url = "https://selenium.dunossauro.live/aula_05.html"
driver = webdriver.Chrome()
driver.get(url)

sleep(5)

path = driver.find_element_by_tag_name('form') #buscando pela tag <form> (onde está localizado nosso formulário)
list_names = ['nome', 'email', 'senha', 'telefone'] #valores do atributo de campo 'name'
for item in list_names:
    resultado = path.find_element_by_name(item) #encontrar pelo atributo 'name'
    inputing = str(input(f'{item} --> ')) #perguntar ao usuário (nome, email, senha e telefone)
    resultado.send_keys(inputing) #escrever o resultado do input pedido no site
resultado = path.find_element_by_name('btn').click() #clicar em enviar formulário

sleep(3)

driver.quit()
