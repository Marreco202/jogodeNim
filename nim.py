#JOGO DE NIM


def start():
    print("=======================")
    print("==== INICIO DO JOGO ====")
    print("=======================\n\n")

    qtd = 12 #quantidade total de bolas no jogo
    i = 0

    print("QUANTIDADE DE BOLINHAS INICIAIS: ",qtd)
    
    while(qtd>0):
        playerRet = playerTurn(qtd)        
        qtd-= playerRet

        nimRet = nimTurn(playerRet,qtd)
        qtd -=nimRet

        update(playerRet,nimRet,qtd)

        update(playerRet,nimRet,qtd)
    return



def nimTurn( pNum,qtd ):
    ret = 4 - pNum
    winCheck(qtd- ret,"Nim")
    return ret




def playerTurn(qtd):
    num = 4 #valor qualquer para bolas retiradas
    while(num > 3):
        num = int(input("Digite a quantidade de bolinhas que deseja retirar: "))
        if(num >3):
            print("ERRO: DIGITE UM NUMERO MENOR OU IGUAL A 3\n")



    winCheck((qtd - num ),"Jogador")
    return num



def update(playerRet, nimRet,qtd):
    print("\nBolinhas retiradas pelo jogador: ",playerRet)
    print("Bolinhas retiradas pelo Nim: ",nimRet)
    print("\nBolas restantes: ",qtd)
    print("\n")
    
    return




def winCheck(num,name):
    if(num <= 0):
        print(" %s ganhou!"%name)
        print("=======================")
        print("==== FIM DE JOGO ======")
        print("=======================\n\n")
        exit()

#main

start()
