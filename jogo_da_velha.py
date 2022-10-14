branco = " "
token = ["X", "O"]

def criarTabuleiro(): #cria o tabuleiro.
    tabuleiro = [
        [branco, branco, branco],
        [branco, branco, branco],
        [branco, branco, branco],
    ]
    return tabuleiro

def printTabuleiro(tabuleiro):
    for i in range(3):
        print("|".join(tabuleiro[i])) #junta os itens separando com um caracter.
        if(i < 2):
            print("------")


def getInputValido(mensagem): #testar a lógica. para verificar se o input está dando certo.
    try:
        n = int(input(mensagem))
        if(n >= 1 and n <= 3):
            return n - 1
        else:
            print("Numero precisa estar entra 1 e 3")
            return getInputValido(mensagem)
    except:
        print("Numero nao valido")
        return getInputValido(mensagem)


def verificaMovimento(tabuleiro, i , j): #Axaminar o movimento.
    if(tabuleiro[i][j] == branco):
        return True
    else:
        return False


def fazMovimento(tabuleiro, i, j, jogador): #Realiza o movimento
    tabuleiro[i][j] = token[jogador]


def verificaGanhador(tabuleiro): # Examinar o ganhador
    # linhas 
    for i in range(3):
        if(tabuleiro[i][0] == tabuleiro[i][1] and tabuleiro[i][1] == tabuleiro[i][2] and tabuleiro[i][0] != branco):
            return tabuleiro[i][0]
    
    # coluna
    for i in range(3):
        if(tabuleiro[0][i] == tabuleiro[1][i] and tabuleiro[1][i] == tabuleiro[2][i] and tabuleiro[0][i] != branco):
            return tabuleiro[0][i]

    # diagonal principal
    if(tabuleiro[0][0] != branco and tabuleiro[0][0] == tabuleiro[1][1] and tabuleiro[1][1] == tabuleiro[2][2]):
        return tabuleiro[0][0]

    # diagonal secundaria
    if(tabuleiro[0][2] != branco and tabuleiro[0][2] == tabuleiro[1][1] and tabuleiro[1][1] == tabuleiro[2][0]):
        return tabuleiro[0][2]

    for i in range(3):
        for j in range(3):
            if(tabuleiro[i][j] == branco):
                return False

    return "EMPATADO"
