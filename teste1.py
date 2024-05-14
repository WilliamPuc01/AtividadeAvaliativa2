from tabulate import tabulate

funcs={}
func = []

def insert():
    matricula = int(input('Numero de Matricula: '))
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
    falta = []
    if pfalta.lower() == 's':
        qtfalta = int(input('Quantas faltas: '))
        renda = renda-(qtfalta*renda/30)
        
            
    else: 
        falta.append('Não possui falta')
        qtFalta=0
    renda=renda-(qtfalta*renda/30)
    imp=0
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


    func=[nome,cod_func,renda,qtfalta,sal,imp*100]
    funcs[matricula]=func
    print(funcs)
def remove():
    rmat=int(input("Digite a matrícula do funcionário que deseja remover: "))
    del funcs [rmat]

n = int(input('Digite a opção: '))
while n>0:
    if(n==1):
        insert()
        n = int(input('Digite a opção: '))
    if(n==2):
        remove()
        n = int(input('Digite a opção: '))
    if(n==3):
        print(funcs)
        break
