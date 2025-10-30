# Crie um dicionário representando informações sobre uma pessoa, como nome, idade e cidade.
import os 

meu_dict = {'Nome': 'Gustavo', 'Idade': 24, 'Cidade': 'Alegre'}
os.system('cls')

for i, (chave, valor) in enumerate(meu_dict.items()):
    print(f'{i + 1} -> {chave}: {valor}')
    print('---------------------')