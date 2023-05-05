from Atividaede.base import *
from time import sleep


url = 'https://selenium.dunossauro.live/exercicio_06.html?nome=n%C3%A3o&senha=nao&l1c0=Enviar%21#'
navegador.get(url)
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

navegador.implicitly_wait(10)

Result = navegador.find_element(By.XPATH,'//*[@id="query"]/h2')
print(Result.text)

for i in  range(0,5):
    chave = navegador.find_element(By.XPATH,xpath_chave)
    input_formulario_nome = navegador.find_element(By.XPATH,xpath_inputs_nomes[chave.text])
    sleep(1)
    input_formulario_nome.send_keys(list_nomes[i])
    input_formulario_senha = navegador.find_element(By.XPATH,xpath_inputs_password[chave.text])
    input_formulario_senha.send_keys(list_pass_word[i])
    sleep(1)
    button_forms = navegador.find_element(By.XPATH, button_xpath[chave.text])
    button_forms.click()
    resutados = navegador.find_element(By.XPATH,resutados_xpath)
    list_resutados.append(eval(resutados.text))
    sleep(1)

print(type( list_resutados[0]))
print(len(list_resutados))