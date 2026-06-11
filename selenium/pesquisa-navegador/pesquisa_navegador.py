from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# iniciando o driver
def iniciar_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    return driver

driver = iniciar_driver()

# acessando o google
def acessa_site():
    url = "https://www.google.com"
    driver.get(url)

# encontrando a caixa de busca
def encontrar_caixa_busca():
    query = "tempo agora contagem"

    try:
        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys(query)
        search_box.submit()
    except Exception as e:
        print("Não encontrado")

# limpando a consulta realizada
def limpar_consulta():
    try:
        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "q"))
        )
        search_box.clear()
    except Exception as e:
        print("Não encontrado")

# fechando o navegador
def fechar_navegador():
    driver.quit()