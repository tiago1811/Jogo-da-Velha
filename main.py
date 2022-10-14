from jogo_da_velha import criarTabuleiro, fazMovimento,  getInputValido, \
                            printTabuleiro, verificaGanhador,  verificaMovimento

from minimax import movimentoIA

jogador = 0 # jogador 1
tabuleiro = criarTabuleiro()
ganhador = verificaGanhador(tabuleiro)
op = 0

print("\n\n     ******MENU*******")
print("          Digite\n")
op = int(input("1 - Jogar contra uma pessoa.\n2 - Jogar contra a IA.\n3 - Ver a IA jogando: "))
print("\n**************")

match op:
    case 1:
        

        while(not ganhador):
            printTabuleiro(tabuleiro)
            print("===================")
            
            i = getInputValido("Digite a linha: ")
            j = getInputValido("Digite a coluna: ")
            
            if(verificaMovimento(tabuleiro, i, j)):
                fazMovimento(tabuleiro, i, j, jogador)
                jogador = (jogador + 1)%2
            else:
                print("A posicao informado ja esta ocupada")
            
            ganhador = verificaGanhador(tabuleiro)
            
        print("===================")
        printTabuleiro(tabuleiro)
        print("Jogador "+ ganhador + " é o vencedor!!!")
        print("===================")
            
    case 2:
        
        while(not ganhador):
            printTabuleiro(tabuleiro)
            print("===================")
            if(jogador == 0):
               i,j = movimentoIA(tabuleiro, jogador)
            else:
                i = getInputValido("Digite a linha: ")
                j = getInputValido("Digite a coluna: ")
            
            if(verificaMovimento(tabuleiro, i, j)):
                fazMovimento(tabuleiro, i, j, jogador)
                jogador = (jogador + 1)%2
            else:
                print("A posicao informado ja esta ocupada")
            
            ganhador = verificaGanhador(tabuleiro)

        print("\n===================")
        printTabuleiro(tabuleiro)
        if(ganhador == "X"):
            ganhador = "Artificial"
        print("\nJogador "+ ganhador + " é o vencedor!!!")
        print("\n===================")
    case 3:
        
        while(not ganhador):
            printTabuleiro(tabuleiro)
            print("===================")
            if(jogador == 0):
               i,j = movimentoIA(tabuleiro, jogador)
            else:
                i,j = movimentoIA(tabuleiro, jogador)
            
            if(verificaMovimento(tabuleiro, i, j)):
                fazMovimento(tabuleiro, i, j, jogador)
                jogador = (jogador + 1)%2
            else:
                print("A posicao informado ja esta ocupada")
            
            ganhador = verificaGanhador(tabuleiro)

        print("\n===================")
        printTabuleiro(tabuleiro)
        print("\n\nJogo "+ ganhador)
        print("\n===================")