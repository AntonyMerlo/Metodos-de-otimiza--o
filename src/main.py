import time

from calculo.VerificacaoPrecedencia import criaPrecedencia
from leitura.LeituraDeInstancia import lerInstancia
from maquinas.CriaMaquinas import armazenarMaquinas
from ultils.Dicionario import CriarDicionario
from ultils.Imprime import imprimeMaquinas
from ultils.solucao import iniciaSolucao, criarSolucao
from calculo.RefinaMaquina import refinarMaquinas
from calculo.heuristicas.HeuristicaTabu import refinarMaquinasTabu
from calculo.heuristicas.HeuristicaDeRefinamento import refinarMaquinas


def main():
    inicio = time.perf_counter() # Marca o início para calcular o tempo

    # Configuração inicial
    qtdMaquinas = [6,10] # [min, max] de maquinas
    
    # "data/HAHN.IN2" or "data/Problema.txt"
    arquivo = "data/HAHN.IN2" 

    # Heurística a utilizar
    # 1 - Heurística padrão
    # 2 - Heurística tabu
    heuristica = 2

    n, custos, precedencias = lerInstancia(arquivo) # Leitura dos dados do arquivo

    # Inicializa variáveis

    # Cria uma lista com n elementos 0
    tarefaConcluidas = [0 for _ in range(n)]
    # Para armazenar a resposta
    resultado = []
    # Para armazenar as maquinas para refinar
    maquinaArmazenada = []

    # Processamento de informações

    # Criar matriz de precedência
    matrizPrecedencia = criaPrecedencia(n, precedencias)
    # Cria um dicionario de termos
    dicionario = CriarDicionario(matrizPrecedencia)
    # Inicia informações
    iniciaSolucao(n, dicionario, matrizPrecedencia, tarefaConcluidas, resultado)
    # Cria solução inicial
    criarSolucao(n, dicionario, tarefaConcluidas, resultado)

    # Refinamento e impressão de resultados

    # Armazena as máquinas
    maquinaArmazenada = armazenarMaquinas(qtdMaquinas, resultado)
    maquinasRefinadas = refinarMaquinas(maquinaArmazenada, custos)
    maquinasRefinadasTabu = refinarMaquinasTabu(maquinasRefinadas, custos)
    # Refina as máquinas armazenadas
    match heuristica:
        case 1:
            
            imprimeMaquinas(maquinaArmazenada, maquinasRefinadas, custos, inicio)
        case 2:
            
            imprimeMaquinas(maquinaArmazenada, maquinasRefinadasTabu, custos, inicio)
        case _:
            print("Opcao invalida")

if __name__ == "__main__":
    main()