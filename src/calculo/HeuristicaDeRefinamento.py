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

# Encontra a melhor solução para cada maquina e retorna a lista das maquinas refinadas
def melhoraMaquina(maquina, custo):
    resultado = copy.deepcopy(maquina)                  # Cria uma cópia de máquina

    for i in range(len(resultado)):
        voltaResultado = copy.deepcopy(resultado)       # Cria uma cópia de resultado
        
        # Move elementos para frente 
        if i+1 < len(resultado):
            x = resultado[i+1].pop(0)                   # Remove o primeiro elemento da próxima máquina
            resultado[i].append(x)                      # Adiciona-o à máquina atual

        maquina, resultado = atualizaOuVolta(maquina, resultado, custo, voltaResultado)

        # Move elementos para trás 
        if i < len(resultado)-1:
            x = resultado[i].pop(len(resultado[i])-1)   # Remove ultimo elemento da maquina
            resultado[i+1].insert(0, x)                 # Adiciona na proxima maquina
        
        maquina, resultado = atualizaOuVolta(maquina, resultado, custo, voltaResultado)

    return maquina

# Refina as maquinas
def refinarMaquinas(maquinaArmazenada, custos):
    maquinasRefinadas = []
    for maquina in maquinaArmazenada:
        maquinaRefinada = melhoraMaquina(maquina, custos)
        maquinasRefinadas.append(maquinaRefinada)
    return maquinasRefinadas