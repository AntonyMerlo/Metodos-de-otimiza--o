import random, copy

from calculo.Vizinhanca import verificarMelhora, gerarVizinhanca


# Busca e melhora de forma que escolha o indice de forma aleatória 
def algoritimoDeBuscaTabu(maxIteracoesSemMelhora, solucaoInicial, custo):

    # Melhor solução obtida até então
    melhorSolucao = copy.deepcopy(solucaoInicial) 
    # Número de iterações
    iteracaoAtual = 0               
    # Última iteração que melhorou
    ultimaMelhoria = 0              
    listaTabu = [] 

    while iteracaoAtual - ultimaMelhoria <= maxIteracoesSemMelhora:
        # Count de interações
        iteracaoAtual +=1

        # Escolhe o indice da maquina a melhorar
        indiceDaMaquina = random.randint(0,len(solucaoInicial)-1)

        # Gera uma nova solução usando a vizinhança 
        novaSolucao = gerarVizinhanca(melhorSolucao, indiceDaMaquina, custo)

        # Atualiza lista tabu
        if novaSolucao not in listaTabu:
            listaTabu.append(novaSolucao)

            # Verificar se a nova solução e melhor que a atual
            if (verificarMelhora(melhorSolucao, novaSolucao, custo)):
                melhorSolucao = novaSolucao
                ultimaMelhoria = iteracaoAtual

    return melhorSolucao

def refinarMaquinasTabu(maquinaArmazenada, custos): 
    maquinasRefinadasTabu = []

    for maquina in maquinaArmazenada:
        # Pela heurística tabu 
        maquinaRefinadaTabu = algoritimoDeBuscaTabu(100000, copy.deepcopy(maquina), custos)
        maquinasRefinadasTabu.append(maquinaRefinadaTabu)

    return maquinasRefinadasTabu