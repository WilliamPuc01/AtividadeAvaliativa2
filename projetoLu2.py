
funcs={}
func=[]

def insert():
    matricula = int(input('Número de Matricula: '))
    while matricula in funcs.keys():
        print('Já existe um funcionário com esse número de matrícula!')
        matricula = int(input('Número de Matricula: '))
    nome = input('Nome p/ Cadastro: ')
    cod_func = int(input('Código da função: '))
    while(cod_func not in (101,102)):
        cod_func = int(input('Código da função: '))
    if(cod_func==101):
        vvendas=float(input("Digite o volume de vendas: "))
        renda=1500+vvendas*0.09
    else:
        renda = float(input('Salário bruto do funcionário: '))
        while(renda<2150 or renda>6950):
            renda = float(input('Salário bruto do funcionário: '))

    pfalta = input('Esse funcionario faltou S/N: ')    
    qtfalta = 0
    if pfalta.lower() == 's':
        qtfalta = int(input('Quantas faltas: '))
        desconto = (qtfalta*(renda/30))
        renda = renda-desconto  
    else: 
        qtfalta=0
        imp=0
        desconto=0
    if(renda<=2259.2):
        imp=0
    elif(renda<=2828.65):
        imp=0.075
    elif(renda<=3751.05):
        imp=0.15
    elif(renda<=4664.68):
        imp=0.225
    else:
        imp=0.275
    sal = renda-renda*imp
    func=[nome,cod_func,renda,qtfalta,sal,imp*100,matricula,desconto]
    funcs[matricula]=func
    print('Funcionário inserido!')
    print('-'*50)   
def remove():
    rmat=int(input("Digite a matrícula do funcionário que deseja remover: "))
    while rmat not in (funcs.keys()):
        print('Matrícula inválida!')
        rmat=int(input("Digite a matrícula do funcionário que deseja remover: "))
    del funcs [rmat]
    print('Funcionário removido!')
    print('-'*50)
def imposto():
    selimp = int(input("Digite a matrícula do funcionário que se deseja determinar a folha de pagamento: "))
    while selimp not in (funcs.keys()):
        print('Não há funcionários com essa matrícula!')
        selimp = int(input("Digite a matrícula do funcionário que se deseja determinar a folha de pagamento: "))
    print(f'Matrícula: {selimp}')
    print(f'Nome: {funcs[selimp][0]}')
    print(f'Código da função:{funcs[selimp][1]}')
    print(f'Salário Bruto do funcionário: {funcs[selimp][2]:.2f}')
    print(f'Salário líquido do funcionário: {funcs[selimp][4]:.2f}')
    print(f'Quantidade de faltas do funcionário: {funcs[selimp][3]}')
    print(f'Porcentagem de imposto: {funcs[selimp][5]:.1f}%')
    print('-'*50)
def relatorio():
    for matricula, dados in funcs.items():
        print(f"Matrícula: {matricula}")
        print(f'Nome: {dados[0]}')
        print(f'Código da função: {dados[1]}')
        print(f"Salário bruto: {dados[2]:.2f}")
        print(f"Salário líquido: {dados[4]:.2f}")
        print('-'*50)
def maiorsal():
    maior = -99999
    for matricula,dados in funcs.items():
        if dados[4] > maior:
            maior = dados[4]
    print(f'Matrícula: {funcs[matricula][6]}')
    print(f'Nome: {funcs[matricula][0]}')
    print(f'Código da função: {funcs[matricula][1]}')
    print(f'Salário bruto: {funcs[matricula][2]:.2f}')
    print(f'Percentual de imposto: {funcs[matricula][5]:.1f}%')
    print(f'Salário líquido: {funcs[matricula][4]:.2f}')
    print('-'*50)
def maisfalta():
    maior = -99999
    for matricula,dados in funcs.items():
        if dados[3] > maior:
            maior = dados[3]
    print(f'Matrícula: {funcs[matricula][6]}')
    print(f'Nome: {funcs[matricula][0]}')
    print(f'Código da função: {funcs[matricula][1]}')
    print(f'Número de faltas: {funcs[matricula][3]}')
    print(f'Desconto no salário: {funcs[matricula][7]} ')
    print('-'*50)
def menu():
    print('1 - Inserir funcionário \n2 - Remover funcionário\n3 - Exibir folha de pagamento de um funcionário\n4 - Relatório do salário bruto e líquido de todos os funcionários\n5 - Imprimir as informações do funcionário com maior salário líquido\n6 - Imprimir as informações do funcionário com o maior número de faltas no mês')
    n = int(input('Digite a opção: '))
    while n not in range(1,7):
        print('Digite uma opção válida!')
        n = int(input('Digite a opção: '))
    print('-'*50)
    return n
        
n = menu()
while True:
    if(n==1):
        insert()     
    if(n==2):
        remove()      
    if(n==3):
        imposto()     
    if n==4:
        relatorio()      
    if n==5:
        maiorsal()
    if n==6:
        maisfalta()
    n = menu()
