import shutil
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv
import os
import time

load_dotenv()

# iniciando o navegador
def iniciar_driver():
    options = webdriver.ChromeOptions()
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    return driver

driver = iniciar_driver()

def acessa_site():
    url = os.getenv('URL')
    driver.get(url)

def acessa_relatorio():
    xpath_relatorios = os.getenv('xpath_relatorios')
    relatorio = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, xpath_relatorios))
    )
    driver.execute_script("arguments[0].click();", relatorio)
    time.sleep(3)  # Aguarda 3 segundos para garantir que a página carregue

def baixa_relatorio():
    xpath_download = os.getenv('xpath_download')
    download = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, xpath_download))
    )
    driver.execute_script("arguments[0].click();", download)
    time.sleep(3)  # Aguarda 3 segundos para garantir que o download seja iniciado

    # cria diretório se não existir para salvar relatório baixado
    projeto = os.getcwd()
    relatorio = os.path.join(projeto, 'relatorio')
    if not os.path.exists(relatorio):
        os.makedirs(relatorio, exist_ok=True)

    try:
        shutil.move(os.path.join(projeto, 'Relatorio_Mensal - HGLG11.xlsx'), relatorio)
    except Exception as e:
        print(f"Erro ao mover o arquivo: {e}")

def fecha_navegador():
    driver.quit()