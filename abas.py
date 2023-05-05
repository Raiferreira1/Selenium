from Atividaede.base import *

def wait_element(By,element,webdriver):
    elements = webdriver.find_elements(By,element)
    print(f'procurando por {element}')
    return bool(elements)


url = 'https://brasilescola.uol.com.br/'
navegador.get(url)

main_window = navegador.current_window_handle

wdw = WebDriverWait(navegador,10)

Ig_button_xpath = '//*[@class="coluna-social"]/li[2]/a'
wdw.until(partial(wait_element,By.XPATH,Ig_button_xpath))
Ig_button = navegador.find_element(By.XPATH,Ig_button_xpath)
Ig_button.click()

while len(navegador.window_handles) == 1:
    continue

for window_handle in navegador.window_handles:
    if window_handle != main_window:
        navegador.switch_to.window(window_handle)
        break

input_button_xpath = '//*[@class="_aauy"]'
wdw.until(partial(wait_element,By.XPATH,input_button_xpath))
input_button = navegador.find_element(By.XPATH,input_button_xpath)
input_button.send_keys('@thv')