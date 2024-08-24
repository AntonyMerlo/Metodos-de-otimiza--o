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
    
    # Encontra o maior comprimento de string na primeira coluna
    maxLen = max(len(f"Maquina normal: {str(maquina[i])}") for i in range(len(maquina)))
    
    for i in range(len(maquina)):
        normalText = f"Maquina normal: {str(maquina[i])}"
        refinadaText = f"Maquina refinada: {str(maquinaRefinada[i])}"
        
        # Alinha as colunas com ljust
        maquinaText += f"{normalText.ljust(maxLen)} \t {refinadaText}\n"

    #Calcula Fo
    foInicial = f"Fo: {str(Fo(maquina, custo))}"
    foRefinado = f"Fo: {str(Fo(maquinaRefinada, custo))}"

    # Marca o fim para calcular o tempo
    fim = time.perf_counter()

    # Alinha o texto do Fo como as colunas anteriores
    maquinaText += f"\n{foInicial.ljust(maxLen)} \t {foRefinado}\n"
    maquinaText += f"Tempo de execucao em milissegundos: {((fim - inicio)*1000):.2f}"

    return maquinaText



def imprimeMaquinas(maquina, maquinaRefinada, custo, inicio):
    linha = "______________________________________________________________________________________________________"
    
    for i in range(len(maquina)):
        print(f"{linha}\n{formataMaquina(maquina[i], maquinaRefinada[i], custo, inicio)}")

    print(linha)