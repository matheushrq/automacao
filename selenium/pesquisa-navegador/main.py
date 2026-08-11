from pesquisa_navegador import acessa_site, acessa_relatorio, baixa_pdf, baixa_relatorio, fecha_navegador

def main():
    acessa_site()
    acessa_relatorio()
    baixa_relatorio()
    baixa_pdf()
    #fecha_navegador()

if __name__ == "__main__":
    main()