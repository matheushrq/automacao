from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def inicia_navegador():
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    options.add_argument('--disable-notifications')
    options.add_argument('--disable-infobars')
    
    navegador = webdriver.Chrome(
        service = Service(ChromeDriverManager().install()), 
        options = options
    )
    return navegador

driver = inicia_navegador()

class AutomacaoMagalu:
    def __init__(self):
        self.driver = driver

    def acessa_site(self):
        url = "https://ri.magazineluiza.com.br/"
        self.driver.get(url)

    def clica_link_planilha(self):
        xpath_pag_inicial = '//*[@id="collapseMobile-3"]/ul/li[2]/a' # sempre coloca o xpath entre aspas simples
        xpath_link = '//*[@id="BvNjWeiZirwEyUUBFST0Iw=="]'

        wait = WebDriverWait(self.driver, 10)
        link_inicial = wait.until(lambda d: d.find_element(By.XPATH, xpath_pag_inicial))
        link_inicial.click()

        link_planilha = wait.until(lambda d: d.find_element(By.XPATH, xpath_link))
        link_planilha.click()

    def fecha_navegador(self):
        self.driver.quit()