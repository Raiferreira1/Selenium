from base import *
from time import sleep

navegador.get('https://selenium.dunossauro.live/exercicio_07.html')

registratio_block_name = 'Faça seu cadastro'
sleep(3)
registratio_block_name_XPTH = '//fieldset/legend'
registratio_block_name_read = navegador.find_element(By.XPATH,registratio_block_name_XPTH)


label_for_name_id = 'lnome'
label_for_name = navegador.find_element(By.ID,label_for_name_id)


input_name_id = 'nome'
input_name = navegador.find_element(By.ID,input_name_id)
input_name.send_keys('Rai Ferreira')

label_for_email_afeter_event = 'Esse email é mesmo valido?'
label_for_email_id = 'lemail'
label_for_email = navegador.find_element(By.ID,label_for_email_id)

input_email_id = 'email'
input_email = navegador.find_element(By.ID,input_email_id)
input_email.send_keys('EliasILoVEjAVA@cANOfluminese')

assert registratio_block_name == registratio_block_name_read.text, f'Erro {registratio_block_name} diferente de {registratio_block_name_read.text}'
assert  label_for_name.text == label_for_name_after_event,f'Erro o eveto desejavel Nao ocorreu'
assert label_for_email.text == label_for_email_afeter_event,f'Erro o evento desejavel Nao ocorreu'
print('passou')
#navegador.quit()