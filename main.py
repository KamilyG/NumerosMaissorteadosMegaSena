import pandas as pd

tabela = pd.read_excel("C:\\loteria\sorteios_loteria.xlsx")     #.loc[:, ['bola1', 'bola2', 'bola3', 'bola4', 'bola5', 'bola6']]
tabela = tabela.values.tolist()
num_sorteados = {}

for linha in range(len(tabela)): # conta a quantidade de vezes que um número apareceu e o adiciona ao dicionário aumentando sua quantidade
    for numero in tabela[linha]:
        if numero in num_sorteados:
            num_sorteados[numero] += 1
        else:
            num_sorteados[numero] = 1

for i in sorted(num_sorteados, key = num_sorteados.get, reverse=True): # printa os dados do dicionários de forma decrescente
    print("O número {} foi sorteado {} vez(es)." .format(i, num_sorteados[i]))
