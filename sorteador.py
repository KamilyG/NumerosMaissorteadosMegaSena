import pandas as pd

tabela = pd.read_excel("C:\\loteria\sorteios_loteria.xlsx") #.loc[:, ['bola1', 'bola2', 'bola3', 'bola4', 'bola5', 'bola6']]
quantidade = 0
tabela = tabela.values.tolist()
num_mais_sorteados = {}

#print(tabela)

for l in range(len(tabela)):
    for n in tabela[l]:
        if n == 13 :
            quantidade += 1
print(quantidade)



#add n to __doc__
#    if n in __doc__
#        n value +1