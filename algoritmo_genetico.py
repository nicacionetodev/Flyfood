import numpy as np
import random

#FUNÇÕES DE CUSTO E APTIDÃO 

def custoCaminho(permutacao, matriz_custos, mapa_indice):
    soma = 0
    R_indice = mapa_indice['R']
    
    v1_indice = mapa_indice[permutacao[0]]
    soma += matriz_custos[R_indice, v1_indice]
    
    for i in range(len(permutacao) - 1):
        a_indice = mapa_indice[permutacao[i]]
        b_indice = mapa_indice[permutacao[i+1]]
        soma += matriz_custos[a_indice, b_indice]
            
    vN_indice = mapa_indice[permutacao[-1]]
    soma += matriz_custos[vN_indice, R_indice]
        
    return soma

def calculaAptidao(populacao, matriz_custos, mapa_indice):
    listaAptidao = []
    listaCustos = []
    
    for individuo in populacao:
        custo = custoCaminho(individuo, matriz_custos, mapa_indice)
        listaCustos.append(custo)
        
        aptidao = 1 / custo
        listaAptidao.append(aptidao)
        
    return listaAptidao, listaCustos

#FUNÇÃO DE PROCESSAMENTO DA MATRIZ

def processar_matriz_de_custos():
    
    NOMES_PONTOS = ['R', 'A', 'B', 'C', 'D']
    NUM_TOTAL_PONTOS = len(NOMES_PONTOS)
    
    DADOS_TRIANGULARES = [
        [3, 2, 5, 7],   
        [3, 4, 4],    
        [3, 5],       
        [2]              
    ]
    
    matriz_custos = np.zeros((NUM_TOTAL_PONTOS, NUM_TOTAL_PONTOS), dtype=int)
    mapa_indice = {nome: i for i, nome in enumerate(NOMES_PONTOS)}
    
   
    for i in range(NUM_TOTAL_PONTOS):
        
        if i >= len(DADOS_TRIANGULARES):
            break
            
        custos_linha = DADOS_TRIANGULARES[i]
        
        for j_offset in range(len(custos_linha)):
            
            j = i + j_offset + 1
            if j >= NUM_TOTAL_PONTOS:
                 break
                 
            peso = custos_linha[j_offset]
            
            matriz_custos[i, j] = peso
            matriz_custos[j, i] = peso 
            
    pontos_interesse = NOMES_PONTOS[1:]
    return matriz_custos, pontos_interesse, mapa_indice

#INICIALIZAR POPULAÇÃO

def inicializar_populacao(tamanho_populacao, pontos_interesse):
    populacao = []
    for _ in range(tamanho_populacao):
        individuo = pontos_interesse[:]
        random.shuffle(individuo)
        populacao.append(individuo)
    return populacao

#FUNÇÃO DE EXECUÇÃO

def iniciar_algoritmo_genetico(tamanho_populacao):
    
    MATRIZ_CUSTOS, PONTOS_INTERESSE, MAPA_INDICE = processar_matriz_de_custos()
    
    populacao_inicial = inicializar_populacao(tamanho_populacao, PONTOS_INTERESSE)
    
    lista_aptidao, lista_custos = calculaAptidao(
        populacao_inicial, MATRIZ_CUSTOS, MAPA_INDICE
    )
    
    melhor_aptidao_indice = np.argmax(lista_aptidao)
    melhor_custo = lista_custos[melhor_aptidao_indice]
    melhor_rota = populacao_inicial[melhor_aptidao_indice]

    print("Matriz de Custos Recebida:")
    print(MATRIZ_CUSTOS)
    print("-" * 30)
    print(f"Total de Pontos a Visitar: {len(PONTOS_INTERESSE)}")
    print("-" * 30)
    print(f"População Inicial (Tamanho: {tamanho_populacao}):")
    
    for i in range(tamanho_populacao):

        marcador = " <--- MELHOR ROTA " if i == melhor_aptidao_indice else ""
        print(f"Rota {i+1}: {populacao_inicial[i]} | Custo: {lista_custos[i]:.2f} | Aptidão: {lista_aptidao[i]:.4f}{marcador}")

    print("-" * 30)
    print(f"Melhor Rota : {['R'] + list(melhor_rota) + ['R']}")
    print(f"Custo Mínimo: {melhor_custo:.2f}")
if __name__ == "__main__":
    iniciar_algoritmo_genetico(tamanho_populacao=15)