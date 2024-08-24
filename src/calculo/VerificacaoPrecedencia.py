def criaPrecedencia(n, precedencias):
    # Inicializa a matriz n x n com zeros
    matriz = []

    #Preenche toda matriz com 0
    for i in range(n):
        linha = [0] * n  # Cria uma linha com n zeros
        matriz.append(linha)
    
    # Preenche as posições indicadas nas precedências com 1
    for predecessora, sucessora in precedencias:
        matriz[predecessora - 1][sucessora - 1] = 1  # Ajuste para índices baseados em 0

    return matriz

# Verifica o inicio
def verificaInicio(matriz, colunaIndex):
    # Verifica se todos os elementos da coluna estão zerados
    for linha in matriz:
        if linha[colunaIndex] != 0:
            return False
    return True

# Verifica se o elemento tem precedente e quantos tem
def verificaPrecedencia(grafo, nProcura):
    qInsidencia = 0
    pontosInsidencia=[]

    for i in grafo:
        for j in range(len(grafo[i])):
            if grafo[i][j] == nProcura:    
                qInsidencia+=1
                pontosInsidencia.append(i)

    return qInsidencia, pontosInsidencia

# Verifica se as precedências estão concluídas
def verificaTarefaPronta(pontosInsidencia, tarefaConcluidas):
    qtd = 0
    for i in range(0,len(pontosInsidencia)):
        if tarefaConcluidas[pontosInsidencia[i]-1] == 1:
            qtd += 1
            if len(pontosInsidencia) == qtd:
                return True
    return False