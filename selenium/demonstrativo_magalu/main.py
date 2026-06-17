from automacao import inicia_navegador, AutomacaoMagalu

def main():
    automacao = AutomacaoMagalu()
    automacao.acessa_site()
    automacao.clica_link_planilha()
    automacao.fecha_navegador()

if __name__ == "__main__":
    main()