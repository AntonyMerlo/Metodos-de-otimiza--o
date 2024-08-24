# Cria o dicionario de termos
def CriarDicionario(matrix):
    dicionario = {}
    
    for i in range(len(matrix)):
        dicionario[i + 1] = []
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1:
                dicionario[i + 1].append(j + 1)
                
    return dicionario