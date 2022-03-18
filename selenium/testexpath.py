from selenium import webdriver
from time import sleep

url = "https://rennerocha.github.io/xpath/"
driver = webdriver.Chrome()
driver.get(url)

path = driver.find_element_by_xpath(f"/html/body//div[@class='pure-g content']") #sempre colocar um 'f' antes do caminho xpath. Quando colocamos '[]' seguido de uma tag, podemos especificar algum atributo dela. Nesse caso temos o '//div[@name_attribute="name"]'.
#quando colocamos '/' estamos indicando o caminho absoluto (não é recomendado pois é muito específico. Há páginas que não contem apenas o html puro, podendo haver JavaScript na maiorias das vezes, deixando a página dinâmica). Quando colocamos '//' ele procura o caminho relativo, então ele procura na árvore inteiro o elemento que corresponde aquele '//'