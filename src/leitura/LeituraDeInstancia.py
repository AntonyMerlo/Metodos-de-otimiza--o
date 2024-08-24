def lerInstancia(arquivo):
    # Abre o arquivo para leitura e garante seu fechamento após a leitura
    with open(arquivo, 'r') as f: # f é o objeto do arquivo usado para ler o conteúdo
        # Lê todas as linhas, remove espaços em branco e ignora linhas vazias

        linhas = [] # linha.strip() for linha in f.readlines() if linha.strip()

        for linha in f.readlines():
            if linha.strip():
                linhas.append(linha.strip())

    # Número de itens
    n = int(linhas[0])
    # Lista de custo
    # Percorra os elementos da lista 'linhas' a partir do índice 1 até o índice 'n'
    # int(linha) = converte strings coletadas do for, que col
    custos = [] # int(linha) for linha in linhas[1:n + 1]
    
    for linha in linhas[1:n + 1]:
        custos.append(int(linha))

    # Inicializa a lista de precedências
    precedencias = []
    # Preenche a lista de precedências
    for linha in linhas[n + 1:]:
        # Interrompe o loop ao encontrar '-1,-1'
        if linha == '-1,-1':
            break
        # Divide a linha e converte os valores para inteiros
        predecessora, sucessora = map(int, linha.split(','))
        # Adiciona a tupla (predecessora, sucessora) à lista
        precedencias.append((predecessora, sucessora))
    
    return n, custos, precedencias