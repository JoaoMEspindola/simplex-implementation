import numpy as np
import time
def primeiroPasso(matrizBase, termosIndependentes):
    return np.linalg.solve(matrizBase, termosIndependentes)

def segundoPasso(matrizBase, coefMatrizBase, matrizNaoBase, coefMatrizNaoBase):
    vetorLambda = np.linalg.solve(np.transpose(matrizBase), coefMatrizBase)
    custoReduzido = 0
    indexVariavelQueEntraBase = -1

    for i in range(len(matrizNaoBase[0])):
        mult = np.dot(np.transpose(vetorLambda), matrizNaoBase[:, i])

        if (coefMatrizNaoBase[i] - mult < custoReduzido):
            custoReduzido = coefMatrizNaoBase[i] - mult
            indexVariavelQueEntraBase = i

    return indexVariavelQueEntraBase

def quartoPasso(matrizBase, matrizNaoBase, indexVariavelQueEntraBase, valorVariaveisBasicas):
    vetorVariavelQueEntra = matrizNaoBase[:, indexVariavelQueEntraBase]

    direcaoSimplex = np.linalg.solve(matrizBase, vetorVariavelQueEntra)
    
    valor = float('inf')
    indexVariavelQueSaiBase = -1

    for i in range(len(valorVariaveisBasicas)):
        if vetorVariavelQueEntra[i] != 0:  # Verificação de divisão por zero
            temp_valor = valorVariaveisBasicas[i] / vetorVariavelQueEntra[i]
            if temp_valor > 0 and temp_valor < valor:
                valor = temp_valor
                indexVariavelQueSaiBase = i

    return indexVariavelQueSaiBase

def sextoPasso(matrizBase, matrizNaoBase, indexVariavelQueEntraBase, indexVariavelQueSaiBase, coefMatrizBase, coefMatrizNaoBase):  

    vetorVariavelQueEntra = np.copy(matrizNaoBase[:, indexVariavelQueEntraBase])
    vetorVariavelQueSai = np.copy(matrizBase[:, indexVariavelQueSaiBase])

    matrizBase[:, indexVariavelQueSaiBase] = vetorVariavelQueEntra

    matrizNaoBase[:, indexVariavelQueEntraBase] = vetorVariavelQueSai

    valor_sai = np.copy(coefMatrizBase[indexVariavelQueSaiBase])
    valor_entra = np.copy(coefMatrizNaoBase[indexVariavelQueEntraBase])

    coefMatrizBase[indexVariavelQueSaiBase] = valor_entra
    coefMatrizNaoBase[indexVariavelQueEntraBase] = valor_sai


    return matrizBase, matrizNaoBase, coefMatrizBase, coefMatrizNaoBase

def simplex(matrizBase, coefMatrizBase, matrizNaoBase, coefMatrizNaoBase, termosIndependentes):
    iteracao = 1
    tempoTotal = 0

    while True:
        ini = time.time()
        
        valorVariaveisBasicas = primeiroPasso(matrizBase, termosIndependentes)
        print(f"Iteração: {iteracao}")
        print(f'Tempo (s): {tempoTotal:.4f}')
        print(f'Objetivo: {sum(valorVariaveisBasicas*coefMatrizBase)}\n')
        
        indexVariavelQueEntraBase = segundoPasso(matrizBase, coefMatrizBase, matrizNaoBase, coefMatrizNaoBase)
        if indexVariavelQueEntraBase == -1:
            fim = time.time()
            tempoTotal += fim-ini
            print(f"Solução ótima encontrada em {tempoTotal:.4f} segundos!\nFunção objetivo é {sum(valorVariaveisBasicas*coefMatrizBase)}.")            
            break

        indexVariavelQueSaiBase = quartoPasso(matrizBase, matrizNaoBase, indexVariavelQueEntraBase, valorVariaveisBasicas)
        matrizBase, matrizNaoBase, coefMatrizBase, coefMatrizNaoBase = sextoPasso(matrizBase, matrizNaoBase, indexVariavelQueEntraBase, indexVariavelQueSaiBase, coefMatrizBase, coefMatrizNaoBase)

        fim = time.time()
        tempoTotal += fim-ini

        iteracao += 1
