def entrar_sistema():
    login = input('Digite seu login: ')
    senha = input('Digite sua senha: ')

    if(login == 'ads' and senha == 'ifpi2019'):
        print('\n')
        print('--------------- BEM VINDO USUÁRIO ------------------')
        print('------------- Sistema Para Advogados ---------------')
        print('\n')
        print(' ________________  MENU PRINCIPAL   _______________ ')
        print('| 1 - Cadastrar Advogado                           |')
        print('| 2 - Listar Advogados                             |')
        print('| 3 - Excluir Advogado                             |')
        print('| 4 - Cadastro de Cliente                          |')
        print('| 5 - Listar Clientes                              |')
        print('| 6 - Excluir Cliente                              |')
        print('| 7 - Inserir Processo                             |')
        print('| 8 - Listar Processo                              |')
        print('| 9 - Excluir Processo                             |')
        print('| 0 - Sair do Sistema                              |')
        print('|__________________________________________________|')

        op = int(input('Digite o número da opção desejada: '))
entrar_sistema()

