#Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.
import os 
os.system('cls')

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
indice = 10

for numero in numeros[::-1]:
    print(numero)

#usando a função reversed
'''
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for numero in reversed(numeros):
    print(numero)
'''