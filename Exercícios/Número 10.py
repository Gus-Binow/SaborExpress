#Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.
import os 
os.system('cls')

nomes = ['Ana','Bia', 'Cora', 'Diogenes', 'Erasmo', 'Flora', 'Gibraltar', 'Honduras', 'Indominus Rex', 'Jacobinos']

for indice, nome in enumerate(nomes):
        print(f'{indice + 1} - {nome}')