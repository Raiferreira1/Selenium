from base import *


def wait_element(By,element,webdriver):
    elements = webdriver.find_elements(By,element)
    print(f'procurando por {element}')
    return bool(elements)


url = 'https://github.com/LuizHenriqueVitorino/python-selenium-notas-de-aula/blob/main/atividades.md'

navegador.get(url)

wdw = WebDriverWait(navegador,10)

wdw.until(partial(wait_element,By.XPATH,'//*[@id="readme"]/article/ol[1]/li/a'))
Teste_link = navegador.find_element(By.XPATH,'//*[@id="readme"]/article/ol[1]/li/a')
Teste_link.click()

wdw.until(partial(wait_element,By.XPATH,"//a[contains(text(),'Access Git Repository (GitHub)')]"))
github_great = navegador.find_element(By.XPATH,"//a[contains(text(),'Access Git Repository (GitHub)')]")
github_great.click()


gitHib_url = 'https://github.com/TestLinkOpenSourceTRMS/testlink-code/tree/testlink_1_9_20_fixed/'

assert  gitHib_url == navegador.current_url, 'Erro'

p = navegador.find_element(By.XPATH,'//input[@class="form-control js-site-search-focus header-search-input jump-to-field js-jump-to-field js-site-search-field is-clearable"]')
p.send_keys('hhjHJ')
p.send_keys(Keys.ENTER)



