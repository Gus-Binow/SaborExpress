# Construa um código que calcule a média dos valores em uma lista. 
# Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.

import os 
os.system('cls')

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
soma = 0
media = 0

try:
    for i in lista:
        soma += i
    media = soma / len(lista)

except ZeroDivisionError:
    print('A lista está vazia e não existe divisão por 0')
    
print('A soma dos elementos da lista é', soma)
print(f'A média dos elementos da lista é {media}')