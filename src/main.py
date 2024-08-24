import time

from calculo.HeuristicaDeRefinamento import refinarMaquinas
from calculo.VerificacaoPrecedencia import criaPrecedencia
from leitura.LeituraDeInstancia import lerInstancia
from maquinas.CriaMaquinas import armazenarMaquinas
from ultils.Dicionario import CriarDicionario
from ultils.Imprime import imprimeMaquinas, imprimeDicionario
from ultils.solucao import iniciaSolucao, criarSolucao

def main():
    inicio = time.perf_counter()                                                   # Marca o início para calcular o tempo

    # Configuração inicial
    qtdMaquinas = [2,5]                                                            # [min, max] de maquinas
    
    # "data/HAHN.IN2" or "data/Problema.txt"
    arquivo = "data/Problema.txt"                                                     

    n, custos, precedencias = lerInstancia(arquivo)                                 # Leitura dos dados do arquivo

    # Inicializa variáveis
    tarefaConcluidas = [0 for _ in range(n)]                                        # Cria uma lista com n elementos 0
    resultado = []                                                                  # Para armazenar a resposta
    maquinaArmazenada = []                                                          # Para armazenar as maquinas para refinar

    # Processamento de informações
    matrizPrecedencia = criaPrecedencia(n, precedencias)                            # Criar matriz de precedência
    dicionario = CriarDicionario(matrizPrecedencia)                                 # Cria um dicionario de termos
    iniciaSolucao(n, dicionario, matrizPrecedencia, tarefaConcluidas, resultado)    # Inicia informações
    criarSolucao(n, dicionario, tarefaConcluidas, resultado)                        # Cria solução inicial

    # Refinamento e impressão de resultados
    maquinaArmazenada = armazenarMaquinas(qtdMaquinas, resultado)                   # Armazena as máquinas
    maquinasRefinadas = refinarMaquinas(maquinaArmazenada, custos)                  # Refina as máquinas armazenadas
    imprimeMaquinas(maquinaArmazenada, maquinasRefinadas, custos, inicio)           # Imprime os resultados da maquina

if __name__ == "__main__":
    main()