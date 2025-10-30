#Crie um dicionário e verifique se uma chave específica existe dentro desse dicionário.
import os 
os.system('cls')

meu_dict = {'Nome': 'Gustavo', 'Idade': 24, 'Cidade': 'Alegre'}

chave = input('Digite a chave que você gostaria e buscar: ')

if chave in meu_dict:
    print('Chave presente no dicionário!\n')
else:
    print('Esta chave não existe no dicionário!\n')