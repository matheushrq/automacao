from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

def inicia_navegador():
    options = webdriver.ChromeOptions()
    navegador = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), 
        options=options
    )
    navegador.maximize_window()
    return navegador

driver = inicia_navegador()

def acessar_site():
    url = "https://www.bstackdemo.com/"
    driver.get(url)

def clica_botao_login():
    botao_login = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "signin"))
    )
    driver.execute_script("arguments[0].click();", botao_login)

def preenche_formulario_dropdown():
    xpath_user = '//*[@id="username"]/div/div[1]'
    xpath_password = '//*[@id="password"]/div/div[1]'
    select_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, xpath_user))
    )
    select = Select(select_element)
    select.select_by_visible_text("demouser")

def fecha_navegador():
    driver.quit()