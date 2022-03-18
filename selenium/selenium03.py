from selenium.webdriver import Chrome
from time import sleep
from urllib.parse import urlparse #biblioteca do python para obter as url's, o selenium por sí só não nos dá essa opção

url = 'http://selenium.dunossauro.live/aula_04_b.html'
driver = Chrome()
driver.get(url)

sleep(5)

def find_elements(browser, tag, text):
    elementos = browser.find_elements_by_tag_name(tag) #buscar pela tag instânciada e armazenar seus valores em 'elementos'
    for elemento in elementos: #percorrer os elementos da lista criada 
        if elemento.text == text: #se o elemento da lista em questão for igual ao texto que nós instânciamos ele nos reternará o elemento em questão 
            return elemento
#Browser = navegador(Chrome)
#Tag = é a tag que eu quero buscar
#Text = conteúdo que deve estar na tag

nome_das_caixas = ['um', 'dois', 'tres', 'quatro']
for numero in nome_das_caixas:
    resultado = find_elements(driver, 'div', numero)
    resultado.click()
sleep(1)
driver.back() #pede para o navegador voltar uma página
sleep(1)
driver.forward() #pede para o navegador andar uma página
#driver.refresh() #recarrega a página, função do f5
#driver.title #exibe o titulo da página (head)

url_parseada = urlparse(driver.current_url) #'urlparse()' é a uma função do urllib, e o '.current_url' é a biblioteca do selenium que nos mostra a url atual
print(url_parseada)

driver.quit()
