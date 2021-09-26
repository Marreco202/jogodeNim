def main():
    print("=======================")
    print("==== INICIO DO JOGO ====")
    print("=======================\n\n")
    qtd= 12
    print("\nQTD INICIAL:", qtd)
    while(qtd>0):
        jogada= int(input("\nInsira qnts deseja retirar:"))
        if(jogada>3 or jogada<1 ):
            print("Número inválido\n")
        else:
            print("\nNim tirou:", 4-jogada)
            qtd -= 4
            print("\ntotal atual:",qtd)
    print("\nNim ganhou!")
    print("=======================")
    print("==== FIM DE JOGO ======")
    print("=======================\n\n")

main()
