import dataManager
import simplex

filename = input()
content = dataManager.readFullFile(f'assets/{filename}.txt')
qntdVariaveis, nmRestricoes, coeficientesFuncaoObjetivo, coeficientesVariaveis, termosIndependentes = dataManager.buildProblem(content)

matrizBase = coeficientesVariaveis[:, -nmRestricoes:] #pega a base factivel inicial
coefMatrizBase = coeficientesFuncaoObjetivo[-nmRestricoes:]

matrizNaoBase = coeficientesVariaveis[:, :(qntdVariaveis-nmRestricoes)]
coefMatrizNaoBase = coeficientesFuncaoObjetivo[:(qntdVariaveis-nmRestricoes)]

simplex.simplex(matrizBase, coefMatrizBase, matrizNaoBase, coefMatrizNaoBase, termosIndependentes)
