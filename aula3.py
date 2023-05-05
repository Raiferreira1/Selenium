from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 


chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico, options=chrome_options)

url = 'https://selenium.dunossauro.live/aula_03.html'

navegador.get(url)
sleep(1)

tag_a ='a'
a = navegador.find_element(By.TAG_NAME,tag_a)

tag_p = 'p'



for i in range(1,11):
    a.click()
    ps = navegador.find_elements(By.TAG_NAME,tag_p)
for i,paragrafo in enumerate(ps):
    print(ps[i].text)
