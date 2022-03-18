import time
from requests import get
from selenium import webdriver
#executar código no Shell:
#start python testeselenium.py  

url = "https://webscraper.io/test-sites/tables"
driver = webdriver.Chrome(executable_path=r'./chromedriver.exe') #executable_path = indica o caminho do webdriver
driver.get(url)

#driver.quit()