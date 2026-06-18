import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def inicia_navegador():
    options = webdriver.ChromeOptions()
    navegador = webdriver.Chrome(
        service = Service(ChromeDriverManager().install()), 
        options = options
    )
    navegador.maximize_window() # inicia o navegador maximizado
    return navegador

driver = inicia_navegador()

class AutomacaoMagalu:
    def __init__(self):
        self.driver = driver

    def acessa_site(self):
        url = "https://ri.magazineluiza.com.br/"
        self.driver.get(url)
        time.sleep(5) # espera 5 segundos para a página carregar completamente

    def clica_link_planilha(self):
        try:
            # sempre colocar o xpath entre aspas simples
            xpath_pag_inicial = '//*[@id="collapseMobile-3"]/ul/li[2]/a'
            xpath_link = '//*[@id="BvNjWeiZirwEyUUBFST0Iw=="]'

            link_pagina = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, xpath_pag_inicial))
            )
            self.driver.execute_script("arguments[0].click();", link_pagina) # clica no link usando JavaScript
            time.sleep(5)

            link_planilha = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, xpath_link))
            )
            self.driver.execute_script("arguments[0].click();", link_planilha)
            time.sleep(10)
            print("Planilha baixada com sucesso!")
        except Exception as e:
            print(f"Erro ao clicar no link da planilha: {e}")

    def fecha_navegador(self):
        self.driver.quit()