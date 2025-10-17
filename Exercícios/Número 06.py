'''Pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else para classificar a idade em categorias de acordo com as seguintes condições:
Criança: 0 a 12 anos;
Adolescente: 13 a 18 anos;
Adulto: acima de 18 anos.
'''
import os
os.system('cls')

faixa_etaria = int(input('Digite sua idade para saber sua classificação etária: '))

if faixa_etaria <= 12:
    print('Você é classificado como criança.')
if faixa_etaria >= 13 and faixa_etaria <= 18: #ou então if 13 <= faixa_etaria <= 18:
    print('Você é classificado como adolescente.')
if faixa_etaria > 18:
    print('Você é classificado como adulto.')