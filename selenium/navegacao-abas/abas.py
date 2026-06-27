from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def inicia_navegador():
    options = webdriver.ChromeOptions()
    servico = Service(ChromeDriverManager().install())

    navegador = webdriver.Chrome(
        service=servico,
        options=options
    )
    navegador.maximize_window()
    return navegador

driver = inicia_navegador()

def acessa_site():
    url = "https://www.google.com.br"
    driver.get(url)

# abrindo link em nova aba
def abre_nova_aba():
    link = driver.find_element(By.XPATH, "//a[@href='https://www.youtube.com.br']")
    driver.execute_script("window.open('');", link)
    driver.switch_to.window(driver.window_handles[-1])

def fecha_navegador():
    driver.quit()