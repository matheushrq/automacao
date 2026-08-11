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
    if not url:
        raise ValueError("A variável de ambiente 'URL' não foi encontrada.")
    driver.get(url)

def _clica_elemento_por_xpath(chave_xpath, timeout=15, espera_pos_click=2):
    xpath = os.getenv(chave_xpath)
    if not xpath:
        raise ValueError(f"A variável de ambiente '{chave_xpath}' não foi encontrada.")

    elemento = WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable((By.XPATH, xpath))
    )
    driver.execute_script("arguments[0].click();", elemento)
    time.sleep(espera_pos_click)

def executa_etapas_xpath(chaves_xpath):
    for chave in chaves_xpath:
        _clica_elemento_por_xpath(chave)

def acessa_relatorio():
    executa_etapas_xpath(['xpath_relatorios'])

def baixa_relatorio():
    executa_etapas_xpath(['xpath_download'])

def baixa_pdf():
    executa_etapas_xpath(['xpath_pdf'])

    # Cria diretório se não existir para salvar relatório baixado.
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