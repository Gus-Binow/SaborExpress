#Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.
import os 
os.system('cls')

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

resultado = 0
impares = []  # lista para armazenar os números ímpares

for numero in numeros:
    if numero % 2 != 0:
        resultado += numero
        impares.append(numero)  # adiciona o número ímpar na lista
    else:
        pass

print("Números ímpares somados:", impares)
print(f'A soma dos números ímpares de 1 a 10 é igual a {resultado}')
