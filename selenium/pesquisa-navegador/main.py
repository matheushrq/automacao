from pesquisa_navegador import acessa_site, encontrar_caixa_busca, fechar_navegador, iniciar_driver, limpar_consulta

def main():
    acessa_site()
    encontrar_caixa_busca()
    limpar_consulta()
    fechar_navegador()

if __name__ == "__main__":
    main()