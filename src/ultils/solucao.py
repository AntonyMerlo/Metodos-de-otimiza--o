from calculo.VerificacaoPrecedencia import verificaPrecedencia, verificaTarefaPronta, verificaInicio

# Inicia a heurística de refinamento
def iniciaSolucao(n, dicionario, matrizPrecedencia, tarefaConcluidas, resultado):
    for i in range(n):
        qInsidencia, pontosInsidencia = verificaPrecedencia(dicionario, i+1)
        if qInsidencia == 0:
            resultado.append(i+1)
        for j in range(n):
            if verificaInicio(matrizPrecedencia, j):
                tarefaConcluidas[j] = 1

# Cria solução inicial Viável
def criarSolucao(n, dicionario, tarefaConcluidas, resultado):
    for i in range(0, n):
        if tarefaConcluidas[i] == 1:
            for executa in range(len(dicionario[i+1])):
                qInsidencia, pontosInsidencia = verificaPrecedencia(dicionario, dicionario[i+1][executa])
                analise = dicionario[i+1][executa]
                v = verificaTarefaPronta(pontosInsidencia, tarefaConcluidas)  # Se o ponto onde ela incide em algo já feito pode ser feito
                if tarefaConcluidas[analise - 1] == 0 and v:
                    resultado.append(analise)
                    tarefaConcluidas[analise-1] = 1