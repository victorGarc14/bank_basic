#sistema bancário com 3 funções depositar, sacar e consultar saldo.
import random


def adicionar_usuario(usuario, lista_usuarios):
    cpf = usuario['cpf']
    for u in lista_usuarios:
        if u['cpf'] == cpf:
            print("Já existe um usuário com este CPF.")
            return
    lista_usuarios.append(usuario)
    print("Usuário adicionado com sucesso.")

def criar_usuario():
    usuario = {}

    usuario['nome'] = input("Digite o nome do usuário: ")
    usuario['data_nascimento'] = input("Digite a data de nascimento (no formato DD/MM/AAAA): ")
    usuario['cpf'] = int(input("Digite o CPF do usuário: "))
    endereco = input("Digite o endereço (no formato logradouro-numero-bairro-cidade/sigla do estado): ")
    usuario['endereco'] = endereco
    usuario['conta'] = criar_conta()

    return usuario
    

def criar_conta():
    conta = {}
    saldo = 0.0
    conta['saldo'] = (saldo)
    conta['numero_conta'] = '{:04}'.format(random.randint(1, 9999))  
    print(f"O número da conta criada é {conta['numero_conta']}")
    return conta


def deposito(acrescimo,saldo):
    saldo+=acrescimo
    depositos = []
    depositos.append(acrescimo)
    return saldo,depositos

def saque(*,LIMITE_SAQUES,saque,saldo,numero_de_saques):
    if numero_de_saques==LIMITE_SAQUES:
        print("Você chegou ao número máximo de saques do dia")
    else:
        saque = float(input("Digite o valor do saque."))
        while saque < 0:
            print("ERRO: Não é possível sacar valores negativos, digite um valor válido")
            saque = float(input("Digite o valor do saque"))
            while saque > 500.0:
                print("Limite de saque é R$500, digite um valor válido.")
                saque = float(input("Digite o valor do saque"))
                if saque > saldo: 
                    print("Saldo insuficiente")
                    continue      
                saldo-=saque
                saques =  []
                saques.append(saque)
                numero_de_saques+=1
    return saldo,numero_de_saques,saques

def extrato(saldo, /,depositos,saques ):
    if len(depositos) != 0:
        print("Depositos")
        for valor_deposito in depositos:
                print(valor_deposito)
    else: print("Não houve depósitos")
    if len(saques) != 0:         
        print("Saques")
        for valor_saque in saques:
                print(valor_saque)
        else: print("Não houve saques")
    print(f"Seu saldo é R${saldo:.2f}")
        
    


numero_de_saques = 0
j = 0
k = 0
entrada = 0
LIMITE_SAQUES = 3
lista_usuarios = []
lista_contas = []
while True:
    print("1.Cadastrar")
    print("2.Entrar")
    print("3.Sair")
    x = int(input("Digite o que deseja realizar:"))

    if x==1:
        usuario = criar_usuario()
        adicionar_usuario(usuario, lista_usuarios)
        lista_contas.append(usuario['conta'])
    
    if x==2:
        cpf = int(input("Digite o CPF "))
        for usuario in lista_usuarios:
            if usuario['cpf'] == cpf:
                saldo = usuario['conta']['saldo']
                print("1.Deposito")
                print("2.Saque")
                print("3.Exibir saldo")
                print("4.Sair")
                n = int(input("Digite o que deseja realizar:"))
                if n>4 or n<0:
                    print("Digite uma opção válida")
                if n == 1:
                    acrescimo = float(input("Digite o valor do deposito"))
                    while acrescimo < 0:
                        print("ERRO: Não é possível depositar valores negativos")
                        acrescimo = float(input("Digite o valor do deposito"))
                    saldo,depositos = deposito(saldo,acrescimo)
                elif n == 2:
                    saldo, saques= saque(LIMITE_SAQUES = 3,saldo = saldo,numero_de_saques=numero_de_saques)
                elif n == 3:
                    extrato(saldo,depositos=depositos,saques=saques)
                elif n == 4:
                    break
            else: print("Usuario não encontrado") 
    if x==3: break    
        
        