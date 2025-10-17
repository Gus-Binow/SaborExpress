#Código para verificar se o número é par ou ímpar
import os
os.system('cls')

verificar_numero = int(input('Digite um número para verificar se é par ou ímpar:\n'))

if verificar_numero % 2 == 0 :
    print('O número é par.')
else:
    print('O número é ímpar.')