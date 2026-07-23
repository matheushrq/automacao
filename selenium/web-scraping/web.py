import requests
from bs4 import BeautifulSoup

def faz_conexao(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("Conexão bem-sucedida!")
            return response.text
    except Exception as e:
        print(f"Tente novamente. Erro: {e}")
        return None

def get_news():
    html = faz_conexao("https://www.globo.com/")
    if html:
        soup = BeautifulSoup(html, 'html.parser')

if __name__ == "__main__":
    get_news()