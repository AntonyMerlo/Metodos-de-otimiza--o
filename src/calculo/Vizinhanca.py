import copy
from .CalculaFo import Fo

# Verifica se o Fo melhorou
def verificarMelhora(maquina, resultado, custo):
    CalculaFoMaquina = Fo(maquina, custo)
    CalculaFoResultado = Fo(resultado, custo)

    return CalculaFoResultado < CalculaFoMaquina

#Verifica e Altera informação se melhorar e retorna atualizado ou volta o mesmo
def atualizaOuVolta(maquina, resultado, custo, voltaResultado):
    if (verificarMelhora(maquina, resultado, custo)):
        return copy.deepcopy(resultado), voltaResultado
    else:
        return maquina, voltaResultado
    
# Função para gerar uma nova vizinhança manipulando a máquina de um determinado índice
def gerarVizinhanca(solucao, indiceMaquina, custo):
    novaSolucao = copy.deepcopy(solucao)
    solucaoAnterior = copy.deepcopy(novaSolucao)

    # Move elementos para frente
    if indiceMaquina + 1 < len(novaSolucao):
        elementoMovido = novaSolucao[indiceMaquina + 1].pop(0)
        novaSolucao[indiceMaquina].append(elementoMovido)

    solucao, novaSolucao = atualizaOuVolta(solucao, novaSolucao, custo, solucaoAnterior)

    # Move elementos para trás
    if indiceMaquina < len(novaSolucao) - 1:
        elementoMovido = novaSolucao[indiceMaquina].pop()
        novaSolucao[indiceMaquina + 1].insert(0, elementoMovido)

    solucao, novaSolucao = atualizaOuVolta(solucao, novaSolucao, custo, solucaoAnterior)

    return solucao