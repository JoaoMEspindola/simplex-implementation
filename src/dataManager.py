import numpy as np
def readFullFile(fileName):
    with open(fileName, 'r') as textFile:
        return textFile.read()
    
def buildProblem(content):
    lines = content.strip().split('\n')
    qntdVariaveis, nmRestricoes = map(int, lines[0].split())

    coeficientesFuncaoObjetivo = np.array(list(map(int, lines[1].split())))

    coeficientesVariaveis = []
    termosIndependentes = []

    for i in range(2, 2 + nmRestricoes):
        line_values = list(map(int, lines[i].split()))
        termosIndependentes.append(line_values.pop())  # Extrai o último valor como termo independente
        coeficientesVariaveis.append(line_values)

    coeficientesVariaveis = np.array(coeficientesVariaveis)
    termosIndependentes = np.array(termosIndependentes)

    return qntdVariaveis, nmRestricoes, coeficientesFuncaoObjetivo, coeficientesVariaveis, termosIndependentes