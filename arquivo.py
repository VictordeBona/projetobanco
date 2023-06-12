menu = '''
[1] Depositar
[2] Sacar
[3] Ver extrato
[0] Sair

=> '''

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)
    
    if opcao == "1":
        valor_deposito = float(input("Operação escolhida: Depósito\nInsira o valor do Depósito: R$ "))
        while(valor_deposito <= 0):
            print("O depósito deve ser um valor positivo!")
            valor_deposito = float(input("Insira o valor do Depósito: R$ "))
        saldo += valor_deposito
        extrato += f"Depósito: R$ {valor_deposito}\n"
        
    elif opcao == "2":
        if numero_saques < LIMITE_SAQUES:
            valor_saque = float(input("Operação escolhida: Saque\nInsira o valor do Saque: R$ "))
            while(valor_saque > 500):
                print("O limite por saque é de R$ 500,00!")
                valor_saque = float(input("Insira o valor do Saque: R$ "))
            while(valor_saque > saldo):
                print("Saldo insuficiente!")
                valor_saque = float(input("Insira o valor do Saque: R$ "))
            while(valor_saque <= 0):
                print("O saque deve ter um valor positivo!")
                valor_saque = float(input("Insira o valor do Saque: R$ "))
            saldo -= valor_saque
            numero_saques += 1
            extrato += f"Saque: R$ -{valor_saque}\n"
        else:
            print("Você atingiu o limite de saques diário!")
        
        
    elif opcao == "3":
        print("Opção escolhida: Extrato")
        extrato += f"Saldo atual: R$ {saldo}"
        print(extrato)
        
    elif opcao == "0":
        print("Obrigado pela preferência!")
        break
    else:
        print("Opção inválida!")
        
        

