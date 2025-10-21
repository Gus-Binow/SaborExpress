import os

restaurantes = ['Pizza', 'Sushi']

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
    print('3 - Ativar restaurante')
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
    os.system('cls')
    #os.system('clear') no mac
    print(texto)
    print()

#voltar ao menu inicial onde se exibe as opções
def voltar_ao_menu():
    input('\nDigite uma tecla para voltar ao menu principal  ')
    main()

#cadastro de novos restaurantes
def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de novo restaurante')

    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    restaurantes.append(nome_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')

    voltar_ao_menu()

#listagem de novos restaurantes
def listar_restaurante():
    exibir_subtitulo('Listando os restaurantes:')

    for indice, restaurante in enumerate(restaurantes):
        print(f'{indice + 1} - {restaurante}')

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
            print('Ativar restaurante')
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