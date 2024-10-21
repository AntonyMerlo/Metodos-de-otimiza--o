import copy

from calculo.heuristicas.HeuristicaDeRefinamento import refinarMaquinas
from calculo.heuristicas.HeuristicaTabu import refinarMaquinasTabu
from ultils.Imprime import imprimeMaquinas

# Refina as maquinas
def refinarMaquinas(maquinaArmazenada, custos):
    a = refinarMaquinas(maquinaArmazenada, custos)
    b = refinarMaquinasTabu(maquinaArmazenada, custos)
    return a, b

