from selenium import webdriver
from Atividaede.base import *                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              

url = 'https://selenium.dunossauro.live/exercicio_06.html?nome=n%C3%A3o&senha=nao&l1c0=Enviar%21#'

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
servico = Service(ChromeDriverManager().install())

wdw = WebDriverWait(navegador,10)



def Achar_elemento(xpath,driver):
    el = driver.find_elements('xpath',xpath)
    return bool(el)

Achar_elemento_dois = partial(Achar_elemento,'//*[@class="form-l0c0"]//input[@name="nome"]')

xpath_inputs_nomes = {
    'l0c0':'//*[@class="form-l0c0"]//input[@name="nome"]',
    'l0c1':'//*[@class="form-l0c1"]//input[@name="nome"]',
    'l1c0':'//*[@class="form-l1c0"]//input[@name="nome"]',
    'l1c1':'//*[@class="form-l1c1"]//input[@name="nome"]'
}
xpath_inputs_password= {
    'l0c0':'//*[@class="form-l0c0"]//input[@name="senha"]',
    'l0c1':'//*[@class="form-l0c1"]//input[@name="senha"]',
    'l1c0':'//*[@class="form-l1c0"]//input[@name="senha"]',
    'l1c1':'//*[@class="form-l1c1"]//input[@name="senha"]'
}
button_xpath = {
    'l0c0':'//*[@class="form-l0c0"]//input[@type="submit"]',
    'l0c1':'//*[@class="form-l0c1"]//input[@type="submit"]',
    'l1c0':'//*[@class="form-l1c0"]//input[@type="submit"]',
    'l1c1':'//*[@class="form-l1c1"]//input[@type="submit"]'
}
list_nomes = ['Elias','Mihh','isa','Flavia','Rai']
list_pass_word = ['2567','7359','1993','7777','1234']

list_resutados = []

xpath_chave = '//*[@id="grid"]//p[2]/span'
resutados_xpath = '//*[@id="query"]//textarea'



wdw.until(partial(Achar_elemento,'//*[@class="form-l0c0"]//input[@name="nome"]'))



   


