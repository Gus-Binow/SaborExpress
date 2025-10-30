#Utilizando o dicionário criado no item 16:
#Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa);
#Adicione um campo de profissão para essa pessoa;
#Remova um item do dicionário.
import os 
os.system('cls')

#dicionário
meu_dict = {'Nome': 'Gustavo', 'Idade': 24, 'Cidade': 'Alegre'}
#versão interativa do código

def alterar_item_dicionario(): #alteração dos itens do dicionário
    chave = input('\nDigite o item que você deseja alterar? (Nome, Idade, Cidade): ')
    if chave in meu_dict:
        novo_valor = input(f'Digite o novo valor para chave {chave}: ')
        meu_dict[chave] = novo_valor
        print("Item alterado com sucesso!\n")
    else:
            print("Essa item não existe no dicionário.\n")

def imprimir_alteração_dict(): #imprimir as opções
    print('Deseja alterar algum item do dicionário?')
    print('Digite 1 para SIM')
    print('Digite 2 para NÃO')

def imprimir_novo_dict(): #imprimir as opções
    print('Deseja adiconar um novo item ao dicionário?')
    print('Digite 1 para SIM')
    print('Digite 2 para NÃO')

def adicionar_item_dict(): #adiconar itens ao dicionário
    chave = input('\nDigite o item a ser adiconado ao dicionário: ')
    nova_chave = input(f'Digite a {chave} que deseja gravar no novo item: ')
    meu_dict[chave] = nova_chave       

def adicionar_outro_item(): #adicionar mais um item ao dicionário
    imprimir_novo_dict()
    novo_item = int(input('Escolha: '))
    while novo_item == 1:
        adicionar_item_dict()
        print('Desejar adicionar outro item ao dicionário?')
        novo_item = int(input('Escolha: '))

imprimir_alteração_dict()
alterar_item= int(input('Escolha: '))

if alterar_item == 1:
    alterar_item_dicionario()

elif alterar_item == 2:
    print('Indo para a próxima etapa...\n')

else:
    print('Opção inválida!\n')
    imprimir_alteração_dict()
    alterar_item_dicionario()

print('-' * 50)
print()

imprimir_novo_dict()
nova_escolha = int(input('Escolha: '))

#adiconando novo item ao dicionário
if nova_escolha == 1:
    adicionar_item_dict()
    print()
    
elif nova_escolha == 2:
    print('Encerrando o programa e imprimindo o dicionário...\n')

else:
    print('Opção inválida!\n')

adicionar_outro_item()

#imprimindo o dicionário
for i, (chave, valor) in enumerate(meu_dict.items()):
    print(f'{i + 1} -> {chave}: {valor}')
    print('--------------------------')


#versão estática do código
'''
#alterando idade
meu_dict['Idade'] = 25

#adcionando profissão
meu_dict['Profissão'] = 'Estudante'

#removendo a cidade
del meu_dict['Cidade']

#imprimindo as informações do dicionário
for i, (chave, valor) in enumerate(meu_dict.items()):
    print(f'{i + 1} -> {chave}: {valor}')
    print('--------------------------')

'''

