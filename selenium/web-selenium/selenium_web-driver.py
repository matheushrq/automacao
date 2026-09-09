from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

def inicia_navegador():
    options = Options()
    navegador = webdriver.Chrome(options=options)
    navegador.maximize_window()

driver = inicia_navegador()

def acessa_site():
    url = "www.google.com.br"
    driver.get(url)
    time.sleep(5)

def finaliza_navegador():
    driver.quit()

if __name__ == "__main__":
    acessa_site()
    finaliza_navegador()