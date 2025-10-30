import os

restaurantes = [{'nome' : 'Praça', 'categoria' : 'Japonesa', 'ativo' : False},
                {'nome' : 'Pizza Suprema', 'categoria' : 'Italiana', 'ativo' : True},
                {'nome' : 'Cantina', 'categoria' : 'Italiana', 'ativo' : False}       
]

#"logo" do aplicativo
def exibir_nome_do_programa():
    print('''
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
''')

#menu de escolha inicial
def exibir_opcoes():
    print('1 - Cadastrar restaurante')
    print('2 - Listar restaurante')
    print('3 - Alternar estado do restaurante')
    print('4 - Sair\n')

#encerrar o app
def finalizar_app():
    exibir_subtitulo('Finalizando o programa')

#o que voltar ao usuário caso a opção seja invalida
def opcao_invalida():
    print('Opção invalida!')
    voltar_ao_menu()

#limpar o prompt e exibir a opção
def exibir_subtitulo(texto):
    os.system('cls') #os.system('clear') no mac
    linha = '*' * (len(texto) + 4)
    print (linha)
    print(texto)
    print (linha)
    print()

#voltar ao menu inicial onde se exibe as opções
def voltar_ao_menu():
    input('\nDigite uma tecla para voltar ao menu principal  ')
    main()

#cadastro de novos restaurantes
def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de novo restaurante')

    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome' :nome_do_restaurante, 'categoria': categoria, 'ativo' : False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')

    voltar_ao_menu()

#listagem de novos restaurantes
def listar_restaurante():
    exibir_subtitulo('Listando os restaurantes:')

    print(f'{'Nome do restaurante'.ljust(24)} | {'Categoria'.ljust(20)} | Status')
    for indice, restaurante in enumerate(restaurantes):
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'Ativado' if restaurante['ativo'] else 'Desativado'
        print(f'{indice + 1} - {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')
    
    voltar_ao_menu()
    
#ativação dos restaurantes cadastrados, já que eles vem por convenção desativados
def altenar_estado_do_restaurante():
    exibir_subtitulo('Alternando estado do restaurante')
    nome_restaurante = input('Digite o nome do restauranta que deseja alterar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')

    voltar_ao_menu()

#escolha uma opção
def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        #opcao_escolhida = int(opcao_escolhida) || outra opção em relação a linha de cima

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurante()
        elif opcao_escolhida == 3:
            altenar_estado_do_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()

    except:
        opcao_invalida()


#alternativo de código no lugar de il elif else
'''
def escolher_opcao():
opcao_escolhida = int(input('Escolha uma opção: '))

match opcao_escolhida:
    case 1:
        print('Cadastrar restaurante')
    case 2:
        print('Listar restaurante')
    case 3:
        print('Ativar restaurante')
    case _:
        finalizar_app()
'''

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()


if __name__ == '__main__':
    main()