#python -i = abre o python no Shell
#python -i (nome do arquivo).py = abre o arquivo e o python no terminal Shell
#exit() = sai do python no Shell
#biblioteca principal = selenium
#biblioteca secundária = webdriver
from selenium.webdriver import Chrome
from time import sleep

url = "https://curso-python-selenium.netlify.app/aula_03.html"
navegador = Chrome() #abrir o chrome webdriver
navegador.get(url) #fazer uma requisição(get) ao url

sleep(6) #o sleep(em segundos) é necessário pois a aplicação demora um certo tempo para carregar toda a página, então sem ele, o nosso script é lido antes mesmo da página carregar, ocasionando em erro

procurar_a = navegador.find_element_by_tag_name('a') #navegador.encontrar_elemento_por_tag_nome("a") = pede para o selenium procurar no HTML do site a tag <a>
procurar_p = navegador.find_element_by_tag_name('p') 
print(f'Conteúdo de <p> em sua posição inicial = {procurar_p.text}') #exibir o conteúdo de <p> inicial

for b in range(0,5): #clicar 5x
    procurar_a.click()
    procurar_ps = navegador.find_elements_by_tag_name('p') #aqui usamos o 'elements' para dizer que <p> tem mais de um valor (lista) e portanto, deve ser lido até o final
    ultimo_elemento_de_p = procurar_ps[-1].text # o '[-1]' serve para que seja exibido somente o último elemento da lista
    print(f'Conteúdo de <p> após o último click = {ultimo_elemento_de_p}') #vai printar todas as atualizações de <p> conforme os clicks são dados

print(f'Conteúdo de <a> = {procurar_a.text}') #printar o conteúdo de <a>
#procurar_a.click() #se eu colar "procurar_a = navegador.find_element_by_tag_name('a')", e executar um "procurar_a.click", ele executa um click na tag <a>
#procurar_a.text #exibe o conteúdo da tag <a>
navegador.quit()


