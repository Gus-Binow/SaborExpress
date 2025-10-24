#Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos.
#Utilize um bloco try-except para lidar com possíveis exceções.
import os 
os.system('cls')

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
soma = 0

def opcao_invalida():
    print('Opção invalida!')


try:
    for numero in numeros:
        if numero >= 0:
            soma += numero
        else:
            pass
    print(f'O valor da soma é: {soma}')

except: opcao_invalida()

