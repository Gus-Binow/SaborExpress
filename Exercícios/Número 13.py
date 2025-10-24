#Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.
import os 
os.system('cls')

tabuada = int(input('Digite um número para ver a tabuada: '))

i = 1
numero = 0
lista = []

print()
print(f'A tabuada do {tabuada} é:')
    
while i <= 10:
    numero = tabuada * i
    lista.append(numero)
    print(f'{tabuada} * {i} = {numero}')
    i += 1
print()