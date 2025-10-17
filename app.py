import os

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
    os.system('cls')
    #os.system('clear') no mac
    print('Finalizando o programa\n')

#escolha uma opção
def escolher_opcao():
    opcao_escolhida = int(input('Escolha uma opção: '))
    #opcao_escolhida = int(opcao_escolhida) || outra opção em relação a linha de cima

    if opcao_escolhida == 1:
        print('Cadastrar restaurante')
    elif opcao_escolhida == 2:
        print('Listar restaurante')
    elif opcao_escolhida == 3:
        print('Ativar restaurante:')
    else:
        finalizar_app()


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
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()


if __name__ == '__main__':
    main()