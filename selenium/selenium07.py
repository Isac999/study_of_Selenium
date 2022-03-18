from time import sleep
from selenium import webdriver

url = "https://selenium.dunossauro.live/aula_05_c.html"
driver = webdriver.Chrome()
driver.get(url)
sleep(2)
names = ['filme','email','telefone']
for item in names:
    result = driver.find_element_by_name(item) #buscando elementos pelo atributo 'name', normalmente usado em formulários onde temos campos de input ao usuário no html
    resposta = str(input(f'Escreva na caixa de texto de {item}: ')) 
    result.send_keys(resposta) #send_keys() é uma função do selenium para entrada de dados (input) na página em questão
driver.find_element_by_name('enviar').click()
