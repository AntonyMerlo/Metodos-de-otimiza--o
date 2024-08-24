# Calcula o Fo
def Calculafo(resultado, custo):
    total = 0

    for i in range(0, len(resultado)):
        total += custo[resultado[i]-1]
        
    return total

# Verificar qual o maior Fo de um array
def Fo(maquina, custos):
    maior = 0

    for i in range(len(maquina)):
        atual = Calculafo(maquina[i], custos)

        if maior < atual:
            maior = atual
    
    return maior