from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
from time import sleep


url = 'https://selenium.dunossauro.live/exercicio_06.html?nome=n%C3%A3o&senha=nao&l1c0=Enviar%21#'


chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico, options=chrome_options)

navegador.get(url)


xpath_inputs_nomes = [
    '//*[@class="form-l0c0"]//input[@name="nome"]',
    '//*[@class="form-l0c1"]//input[@name="nome"]',
    '//*[@class="form-l1c0"]//input[@name="nome"]',
    '//*[@class="form-l1c1"]//input[@name="nome"]'
    ]


xpath_inputs_password= [
    '//*[@class="form-l0c0"]//input[@name="senha"]',
    '//*[@class="form-l0c1"]//input[@name="senha"]',
    '//*[@class="form-l1c0"]//input[@name="senha"]',
    '//*[@class="form-l1c1"]//input[@name="senha"]'
]

button_xpath = [
    '//*[@class="form-l0c0"]//input[@type="submit"]',
    '//*[@class="form-l0c1"]//input[@type="submit"]',
    '//*[@class="form-l1c0"]//input[@type="submit"]',
    '//*[@class="form-l1c1"]//input[@type="submit"]'
]


list_nomes = ['Elias','Mihh','isa','Flavia']
list_pass_word = ['2567','7359','1993','7777']



'//*[@id="grid"]//span'
sleep(5)
for i in  range(0,5):
    input_formulario_nome = navegador.find_element(By.XPATH,xpath_inputs_nomes[i])
    input_formulario_nome.send_keys(list_nomes[i])
    input_formulario_senha = navegador.find_element(By.XPATH,xpath_inputs_password[i])
    input_formulario_senha.send_keys(list_pass_word[i])
    button_forms = navegador.find_element(By.XPATH, button_xpath[i])
    button_forms.click()
    sleep(3)