from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
from time import sleep

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico, options=chrome_options)
navegador.get('https://www.amazon.com.br')


ID_Input = 'twotabsearchtextbox'
pesquisa = 'livro harry potter'
input = navegador.find_element(By.ID, ID_Input)

input.send_keys(pesquisa)
input.send_keys(Keys.ENTER)

sleep(2)

Resutado_xpath = '//h1/div/div[1]/div/div/span[3]'
Resutado = navegador.find_element(By.XPATH,Resutado_xpath)

if Resutado.text == '"'+pesquisa+'"':
    print('OK')
else:
    print('Não')

#navegador.quit()