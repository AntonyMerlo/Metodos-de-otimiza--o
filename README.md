# Métodos de Otimização

Este projeto implementa métodos de otimização para resolver problemas práticos utilizando heurísticas gulosas. O objetivo é analisar dados, identificar requisitos e aplicar uma solução que minimize o custo total de execução. O projeto foi desenvolvido em Python.

## Introdução

Neste trabalho, utilizamos uma heurística gulosa para obter uma solução inicial para o problema. O objetivo é mostrar como é possível chegar a uma solução viável que, posteriormente, pode ser refinada.

## Conteúdo

### Heurística Gulosa

A heurística gulosa é uma abordagem onde selecionamos elementos candidatos para inserção no conjunto solução da seguinte forma:
- **Conjunto Candidato**: Conjunto extraído dos arquivos dentro do diretório `data`, usado para criar a solução do problema.
- **Seleção**: Selecionamos um elemento e verificamos sua viabilidade.
- **Viabilidade**: Verificamos se o elemento não fere suas precedências para entrar no conjunto solução.
- **Função Objetivo (FO)**: Atribuímos um valor de custo para a solução.
- **Solução**: Uma solução viável para o problema.

Problemas clássicos resolvidos com esta heurística incluem o problema da mochila, onde o objetivo é maximizar o valor dos itens colocados em uma mochila de tamanho limitado.

### Solução Inicial

<div align="center">
    <img src="./img/GrafoDePrioridades.png" alt="Grafo de Prioridades">
    <br>
    <figcaption>Figura 1 - Grafo de Prioridades</figcaption>
</div>

A Figura 1 mostra um grafo de prioridades, representando a ordem de execução das tarefas, onde cada número corresponde a uma tarefa e as arestas indicam precedência. Cada tarefa tem um custo atribuído a ela, e nenhuma tarefa pode ser concluída se sua antecessora não for finalizada.

Solução inicial viável: `[1, 2, 3, 4, 8, 6, 7, 9, 5]`

<div align="center">
    <img src="./img/GrafoDePrioridadesComCusto.png" alt="Grafo de Prioridades com Custo">
    <br>
    <figcaption>Figura 2 - Grafo de Prioridades com Custo</figcaption>
</div>

A Figura 2 mostra o mesmo grafo, mas com o custo de cada tarefa. O custo total para a execução das tarefas é 42. Dividimos as tarefas em várias máquinas, simulando uma linha de produção.

<div align="center">
    <img src="./img/LinhaDeMontagem.png" alt="Linha de Montagem">
    <br>
    <figcaption>Figura 3 - Linha de Montagem</figcaption>
</div>

Cada operador é atribuído a um conjunto de tarefas. Queremos melhorar a Função Objetivo (FO) atribuindo tarefas de maneira equilibrada entre os operadores.
#### Representação de Máquinas:
##### Maquina não refinada:
```
Quantidade de maquinas: 5

Maquina normal: [1, 2]
Maquina normal: [3, 4]
Maquina normal: [8, 6]
Maquina normal: [7, 9]
Maquina normal: [5]   

Fo: 12
```
A função objetivo (FO) é calculada considerando o custo mais alto entre todas as máquinas.

##### Maquina refinada:
```
Quantidade de maquinas: 5

Maquina refinada: [1]
Maquina refinada: [2, 3]
Maquina refinada: [4, 8, 6]
Maquina refinada: [7, 9]
Maquina refinada: [5]

Fo: 11

```
Após refinamento usando a política de vizinhança, obtivemos um valor melhor, mostrando uma melhora na solução inicial.

A política de vizinhança consiste em mover o último elemento, removendo-o da lista e alocando-o na primeira posição da lista inferior, e também fazendo o caminho contrário, sempre buscando o melhor valor possível para a função objetivo (FO).
