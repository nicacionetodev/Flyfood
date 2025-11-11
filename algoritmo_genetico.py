import numpy as np
import random
import math

# Função para calcular a distância euclidiana 
def calcular_distancia_euclideana(coordenada1, coordenada2):
    x1, y1 = coordenada1
    x2, y2 = coordenada2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Simulação 
def processar_matriz():

    coordenadas = {
        'R': (0, 0),
        'A': (1, 2),
        'B': (2, 3),
        'C': (3, 4),
        'D': (4, 5)
    }
    
    pontos_nomes = list(coordenadas.keys()) 
    num_pontos = len(pontos_nomes)
    matriz_custos = np.zeros((num_pontos, num_pontos))

    mapa_indice = {nome: i for i, nome in enumerate(pontos_nomes)}

    for i_nome in pontos_nomes:
        i = mapa_indice[i_nome] 
        
        for j_nome in pontos_nomes:
            j = mapa_indice[j_nome] 
            
            if i != j:
                
                custo = calcular_distancia_euclideana(coordenadas[i_nome], coordenadas[j_nome])
                
                matriz_custos[i, j] = custo
                
    return matriz_custos, pontos_nomes[1:]

MATRIZ_CUSTOS, PONTOS_INTERESSE = processar_matriz()
QTDE_PONTOS = len(PONTOS_INTERESSE)

# Algoritmo Genético
def inicializar_populacao(tamanho_populacao, pontos_interesse):
    populacao = []
    for _ in range(tamanho_populacao):
        individuo = pontos_interesse[:]
        random.shuffle(individuo)
        populacao.append(individuo)
    return populacao

TAMANHO_POPULACAO = 100
populacao_inicial = inicializar_populacao(TAMANHO_POPULACAO, PONTOS_INTERESSE)
print("Matriz de Custos:")
print(MATRIZ_CUSTOS.round(0))
print("\n População Inicial:",TAMANHO_POPULACAO)
for i,rota in enumerate(populacao_inicial):
    print(f"Rota {i+1}: {rota}")