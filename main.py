import pandas as pd

tabela = pd.read_excel("C:\\loteria\sorteios_loteria.xlsx")     #.loc[:, ['bola1', 'bola2', 'bola3', 'bola4', 'bola5', 'bola6']]
tabela = tabela.values.tolist()
num_mais_sorteados = {}

def calcular_quantidade():
    for l in range(len(tabela)):
        for n in tabela[l]:
            if n in num_mais_sorteados:
                num_mais_sorteados[n] += 1
            else:
                num_mais_sorteados[n] = 1

print(num_mais_sorteados)