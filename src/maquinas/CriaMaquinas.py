def criaMaquinas(qtd, valores):
    lista = []
    tam = len(valores) // qtd                           # Tamanho básico de cada sub-lista
    resto = len(valores) % qtd                          # Elementos restantes que precisam ser distribuídos

    inicio = 0
    for i in range(qtd):
        fim = inicio + tam + (1 if i < resto else 0)    # Distribui os elementos restantes
        lista.append(valores[inicio:fim])
        inicio = fim

    return lista

def armazenarMaquinas(qtdMaquinas, resultado):
    maquinaArmazenada = []
    for i in range(qtdMaquinas[0]-1, qtdMaquinas[1]):
        maquinaArmazenada.append(criaMaquinas(i+1, resultado))
    
    return maquinaArmazenada