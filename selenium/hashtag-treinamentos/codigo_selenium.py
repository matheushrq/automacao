from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time

def inicia_navegador():
    options = webdriver.ChromeOptions()
    navegador = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    navegador.maximize_window()
    return navegador

driver = inicia_navegador()

def acessa_site():
    url = "https://www.hashtagtreinamentos.com"  # Substitua pelo URL desejado
    driver.get(url)

def localiza_elemento():
    driver.find_element()