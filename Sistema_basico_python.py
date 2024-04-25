#sistema bancário com 3 funções depositar, sacar e consultar saldo.
n = 0
saldo=0.0
i = 0
j = 0
k = 0
LIMITE_SAQUES = 3
depositos =[]
saques = []
while True:
    print("1.Deposito")
    print("2.Saque")
    print("3.Exibir saldo")
    print("4.Sair")
    n = int(input("Digite o que deseja realizar:"))
    if n>4 or n<0:
        print("Digite uma opção válida")
        continue    
    
    if n == 1:
        acrescimo = float(input("Digite o valor do deposito"))
        while acrescimo < 0:
            print("ERRO: Não é possível depositar valores negativos")
            acrescimo = float(input("Digite o valor do deposito"))
        saldo+=acrescimo
        depositos.append(acrescimo)
    elif n == 2:
        if i==LIMITE_SAQUES:
            print("Você chegou ao número máximo de saques do dia")
            continue
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
            saques.append(saque)
            i+=1
    elif n == 3:
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
    elif n == 4:
        break
        
        
        
        