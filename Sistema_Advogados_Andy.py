print('\n')
print(' -----------   ESCRITÓRIO DE ADVOCACIA  ---------------' )
print(' ----------  Advocavia Santos & Silva  ----------------' )
print(' Tel: (89) 981322664      e-mail: andy_elves@outlook.com')
print('\n')
print(' DIREITO CIVIL  |  DIREITO EMPRESARIAL  |  DIREITO DO CONSUMIDOR |')
print(' DIREITO DA TECNOLOGIA DA INFORMAÇÃO  |    DIREITO TRIBUTÁRIO    |')
print(' DIREITO ADMINISTRATIVO   | DIREITO TRABALHISTA ')
print(' DIREITO PREVIDENCIÁRIO   | DIREITO PENAL ')



def sistema_advogados():
    arquivo = open('Advogados.txt','a')
    arquivo.close()
def sistema_clientes():
    arquivo = open('Clientes.txt','a')
    arquivo.close()

def cadastrar_advogado():
    arquivo = open('Advogados.txt','a')
    
    print('CADASTRO DE ADVOGADO: \n')
    advogados = []
    nome = input('Nome do advogado: ')
    oab = input('Registro na oab: ')
    especialidade = input('Especialidade: ')
    telefone = input('Tefelone de contato: ')
    email = input('E-mail: ')
    advogados.append([nome,oab,especialidade,telefone,email])
    for i in advogados:
        arquivo.write('%s - %s - %s - %s - %s\n' %(i[0],i[1],i[2],i[3],i[4]))
        arquivo.close()

def mostrar_advogado():
    advogados = []
    arquivo = open('Advogados.txt','r')
    for l in arquivo.readlines():
        nome,oab,especialidade,telefone,email= l.strip().split('-')
        advogados.append([nome, oab, especialidade, telefone, email])
    arquivo.close()

    print('\n Lista de advogados Cadastrados no Sistema:\n\n')
    print('Escolha um que se enquadre ao seu problema! Em seguida, siga as instruções.')
    i = 1
    for e in advogados:
        print(i,'nome: %s oab: %s especialidade: %s telefone: %s email: %s' % (e[0],e[1],e[2],e[3],e[4]))
        i = i+1

        


def remover_advogado():
    arquivo = open('Advogados.txt','r')
    advogados= []
    for l in arquivo.readlines():
        nome,oab,especialidade,telefone,email = l.strip().split('-')
        advogados.append([nome, oab, especialidade, telefone, email])
    arquivo.close()
    mostrar_advogado()
    idcontato= int(input('Digite o ID do Advogado: '))
    del advogados[idcontato]

    arquivo = open('Advogados.txt','w')
    for i in advogados:
         arquivo.write('%S - %s - %s - %s - %s\n' % (i[0],i[1],i[2],i[3],i[4]))
    arquivo.close()



def cadastrar_cliente():
    arquivo = open('Clientes.txt','a')
    cliente = []
    
    nome = input('Nome do Cliente: ')
    cpf = input('Número de CPF: ')
    cliente.append([nome,cpf])
    for i in cliente:
        arquivo.write('%s - %s'% (i[0],i[1]))

    arquivo.close()

def mostrar_cliente():
    arquivo = open('Clientes.txt','r')
    clientes = []
    for l in arquivo.readlines():
        nome,cpf = l.strip().split('-')
        clientes.append([nome,cpf])
    arquivo.close()

    print('\n Lista de Clientes: \n\n')
    i = 1
    for e in clientes:
        print(i,'nome: %s cpf: %s' % (e[0],e[1]))
        i = i+1
def excluir_cliente():
    arquivo = open('Clientes.txt','r')
    clientes = []
    for l in arquivo.readlines():
        nome,cpf = l.strip().split('-')
        clientes.append([nome, cpf])
    arquivo.close()
    mostrar_cliente()
    idcontato= int(input('Digite o ID do cliente: '))
    del clientes[idcontato]

    arquivo = open('Clientes.txt','w')
    for i in clientes:
         arquivo.write('%S - %s - %s - %s - %s\n' % (i[0],i[1]))
    arquivo.close()
    
    

def inserir_processo():
    processo = []
    arquivo = open('Processos.txt','a')

    mostrar_advogado()
    advogado = input('Nome do advogado responsável: ')
    oab = input('Digite o registro OAB do advogado: ')
    data = input('Insira a data de início do processo: ')
    processo.append([advogado,oab,data])
    for i in processo:
        arquivo.write('%s - %s - %s'% (i[0],i[1],i[2]))
    arquivo.close()

def mostrar_processos():
    arquivo = open('Processos.txt','r')
    processos = []
    for l in arquivo.readlines():
        advogado,oab,data = l.strip().split('-')
        processos.append([advogado,oab,data])
    arquivo.close()

    print('\n Lista de Processos: \n\n')
    i = 1
    for e in processos:
        print(i,'advogado: %s oab: %s data: %s' % (e[0],e[1], e[2]))
        i = i+1

def excluir_processo():
    arquivo = open('Processos.txt','r')
    processos = []
    for l in arquivo.readlines():
        advogado,oab,data = l.strip().split('-')
        processos.append([advogado,oab,data])
    arquivo.close()
    mostrar_processo()
    idcontato= int(input('Digite o ID do cliente: '))
    del clientes[idcontato]

    arquivo = open('Clientes.txt','w')
    for i in clientes:
         arquivo.write('%S - %s - %s - %s - %s\n' % (i[0],i[1]))
    arquivo.close()
    
def entrar_sistema():
    print('\n')
    print('OLÁ! PREZADO USUÁRIO, INSIRA O SEU LONGIN E SUA SENHA, PARA TER ACESSO AO AMBIENTE\n DE INTERAÇÃO DO MENU PRINCIPAL!')
    print('\n')
    login = input('Digite seu LOGIN: ')
    senha = input('Digite sua SENHA: ')

    if(login == 'ads' and senha == 'ifpi2019'):
        print('\n')
        print('--------------- BEM VINDO USUÁRIO ------------------')
        print('------ Sistema Para Escritório de Advocacia --------')
        print('\n')
        print(' ________________  MENU PRINCIPAL   _______________ ')
        print('|                                                  |')
        print('| 1 - Cadastrar Advogado                           |')
        print('| 2 - Listar Advogados                             |')
        print('| 3 - Excluir Advogado                             |')
        print('| 4 - Cadastro de Cliente                          |')
        print('| 5 - Listar Clientes                              |')
        print('| 6 - Excluir Cliente                              |')
        print('| 7 - Criar Processo                               |')
        print('| 8 - Listar Processo                              |')
        print('| 9 - Excluir Processo                             |')
        print('| 0 - Sair do Sistema                              |')
        print('|__________________________________________________|')
        print('\n')

        op = int(input('Digite o número da opção desejada: '))

        if(op==1):
            cadastrar_advogado()
            print('ADVOGADO CADASTRADO!\n')

        if(op==2):
            print('ADVOGADOS CADASTRADOS NO SISTEMA: \n')
            mostrar_advogado()
            
        if(op==3):
            print('EXCLUINDO ADVOGADO\n')
            remover_advogado()
            print('ADVOGADO EXCLUÍDO!\n')

        if(op==4):
            print('CADASTRO DE CLIENTE: \n')
            cadastrar_cliente()
            print('CLIENTE CADASTRADO!\n')
            

        if(op==5):
            print('CLIENTES CADASTRADOS NO SISTEMA: \n')
            mostrar_cliente()
            
        if(op==6):
            print('EXCLUINDO CLIENTE\n')
            excluir_cliente()
            print('CLIENTE EXCLUÍDO!\n')

        if(op==7):
            print('SOLICITAÇÃO DE PROCESSO: \n')
            inserir_processo()
            print('PROCESSO CADASTRADO!\n')
            
        if(op==8):
            print('LISTA DE PROCESSOS: \n')
            mostrar_processos()
            mostrar_cliente()
        if(op==9):
            print('EXCLUINDO PROCESSO: \n')
            excluir_processo()
        
        if(op==0):
            nota = int(input('Caro cliente, antes de sair, atribua uma nota aos nossos serviços: '))
            print(' A nota digitada foi: ',nota)
            print('Obrigado. Volte sempre! o/')
    elif(login != 'ads' and senha != 'ifpi2019'):
        print('A SENHA, OU LOGIN DIGITADO ESTÁ INCORRETO!')
        print('TENTE NOVAMENTE: ')
        entrar_sistema()
            

entrar_sistema()


