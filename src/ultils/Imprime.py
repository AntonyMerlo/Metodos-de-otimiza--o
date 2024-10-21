import time

from calculo.CalculaFo import Fo

def imprimeDicionario(dicionario):
    for no in dicionario:
        coneccoes = ', '.join(map(str, dicionario[no]))
        print(f"{no} -> {coneccoes if coneccoes else 'Nenhum'}")

def imprimeMatriz(matriz):
    print("Matriz:\n")
    for linha in matriz:
        print(linha)

def formataMaquina(maquina, maquinaRefinada, custo, inicio):
    maquinaText = f"\nQuantidade de maquinas: {len(maquina)}\n\n"
    
    # Calcula o maior comprimento de todas as colunas em todas as linhas
    maxLenNormal = max(len(f"Maquina normal: {str(maquina[i])}") for i in range(len(maquina)))
    maxLenRefinada = max(len(f"Maquina refinada: {str(maquinaRefinada[i])}") for i in range(len(maquina)))

    # Para cada máquina, alinhar os textos com base nos maiores comprimentos calculados
    for i in range(len(maquina)):
        normalText = f"Maquina normal: {str(maquina[i])}"
        refinadaText = f"Maquina refinada: {str(maquinaRefinada[i])}"
        
        # Alinha as colunas com base nos maiores comprimentos globais
        maquinaText += f"{normalText.ljust(maxLenNormal)}\t{refinadaText.ljust(maxLenRefinada)}\n"

    # Calcula Fo
    foInicial = f"Fo: {str(Fo(maquina, custo))}"
    foRefinado = f"Fo: {str(Fo(maquinaRefinada, custo))}"
    # Marca o fim para calcular o tempo
    fim = time.perf_counter()

    # Alinha o texto do Fo como as colunas anteriores, com base no maior comprimento das colunas de máquinas
    maquinaText += f"\n{foInicial.ljust(maxLenNormal)}\t{foRefinado.ljust(maxLenRefinada)}\n"
    
    maquinaText += f"Tempo de execucao em milissegundos: {((fim - inicio) * 1000):.2f} ms"

    return maquinaText


def imprimeMaquinas(maquina, maquinaRefinada, custo, inicio):
    linha = "______________________________________________________________________________________________________"
    
    for i in range(len(maquina)):
        print(f"{linha}\n{formataMaquina(maquina[i], maquinaRefinada[i], custo, inicio)}")

    print(linha)