'''
Solicite um nome de usuário e uma senha e use uma estrutura
if else para verificar se o nome de usuário e a senha fornecidos
correspondem aos valores esperados determinados por você.
'''
import os
os.system('cls')

nome_de_usuario = str(input('Digite um nome de usuário de no mínimo 8 caracteres: ')) 
senha_do_usuario = str(input('\nDigite uma senha de no mínimo 8 caracteres: '))

if len(nome_de_usuario) and len(senha_do_usuario) >= 8:
    print('Usuário e senha aceitos')
else:
    print('Usuário ou senha diferentes do que foi pedido.')