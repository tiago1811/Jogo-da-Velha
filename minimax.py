from jogo_da_velha import branco, token, verificaGanhador

def movimentoIA(tabuleiro, jogador):
    possibilidades = getPosicoes(tabuleiro)
    melhor_valor = None #None == falta de valor.
    melhor_movimento = None
    for possibilidade in possibilidades:
        tabuleiro[possibilidade[0]][possibilidade[1]] = token[jogador] #acessando a lista na função getPosições.
        valor = minimax(tabuleiro, jogador) # A função MinMax vai retornar o valor 1, 0 ou -1.
        tabuleiro[possibilidade[0]][possibilidade[1]] = branco #Reset para não deixar que todas as posições sejam "X".
        if(melhor_valor is None):
            melhor_valor = valor
            melhor_movimento = possibilidade
        elif(jogador == 0):# Jogador 0 é X.
            if(valor > melhor_valor):
                melhor_valor = valor
                melhor_movimento = possibilidade
        elif(jogador == 1): # Jogador 1 é O.
            if(valor < melhor_valor):
                melhor_valor = valor
                melhor_movimento = possibilidade
        print(possibilidade, melhor_valor)
    return melhor_movimento[0], melhor_movimento[1]   #Va retornar o melhor movimento

def getPosicoes(tabuleiro): #pega todas as posições vazias
    posicoes = []
    for i in range(3):
        for j in range(3):
            if(tabuleiro[i][j] == branco):
                posicoes.append([i, j]) #coodenada
    
    return posicoes

score = {
    "EMPATADO": 0,
    "X": 1,
    "O": -1
}

def minimax(tabuleiro, jogador):
    ganhador = verificaGanhador(tabuleiro)
    if(ganhador):
        return score[ganhador]
    jogador = (jogador + 1)%2
    
    possibilidades = getPosicoes(tabuleiro)
    melhor_valor = None
    for possibilidade in possibilidades:
        tabuleiro[possibilidade[0]][possibilidade[1]] = token[jogador]
        valor = minimax(tabuleiro, jogador)
        tabuleiro[possibilidade[0]][possibilidade[1]] = branco

        if(melhor_valor is None):
            melhor_valor = valor
        elif(jogador == 0):
            if(valor > melhor_valor):
                melhor_valor = valor
        elif(jogador == 1):
            if(valor < melhor_valor):
                melhor_valor = valor

    return melhor_valor