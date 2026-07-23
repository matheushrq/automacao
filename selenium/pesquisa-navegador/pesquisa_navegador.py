from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv
import os

load_dotenv()

# iniciando o driver
def iniciar_driver():
    options = webdriver.ChromeOptions()
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    return driver

driver = iniciar_driver()

def acessa_site():
    url = "https://www.youtube.com"
    driver.get(url)

def encontrar_caixa_busca():
    pesquisar = os.getenv("BOTAO_PESQUISAR")
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "search_query"))
    )
    search_box.send_keys("how to use selenium with python")

    realiza_pesquisa = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, pesquisar))
    )
    driver.execute_script("arguments[0].click();", realiza_pesquisa)

def fechar_navegador():
    driver.quit()

if __name__ == "__main__":
    acessa_site()
    encontrar_caixa_busca()
    # fechar_navegador()