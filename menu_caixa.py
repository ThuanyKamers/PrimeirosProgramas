menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=>"""

saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)
    print(f"Opção escolhida: {opcao}")

    if opcao == "1":
        print("Depósito")

        try:
            deposito = float(input("Valor do depósito: "))
            if deposito > 0:
                print("O valor do depósito é: ", deposito)
                saldo += deposito
                extrato.append(f"Depósito: R${deposito:.2f}")
                print(f"O valor do depósito é: R${deposito:.2f}")
                print(f"Saldo atualizado: R${saldo:.2f}")
            else:
                print("Não é possível depositar valor negativo.")
        except ValueError:
            print("Entrada inválida, por favor insira um número.")

    elif opcao == "2":
        if numero_saques < LIMITE_SAQUES:
            print ("Saque")
        
            try:
                saque = float(input("Valor do saque: "))
                if saque > 0:
                    if saque <= saldo and saque <= limite:
                        saldo -= saque
                        extrato.append(f"Saque: R${saque:.2f}")
                        print(f"O valor do saque é: R${saque:.2f}")
                        print(f"Saldo atualizado: R${saldo:.2f}")
                        numero_saques += 1
                    elif saque > limite:
                        print(f"Limite de saque diário é de: R${limite:.2f}")
                    else:
                        print("Saldo insuficiente.")
                else:
                    print("Não é possível sacar valor negativo.")
            except ValueError:
                print("Entrada inválida, por favor insira um número.")    
        else:
            print("Limite de saques diários atingido. Você não pode realizar mais saques hoje.")                      

    elif opcao == "3":
        print("Extrato")
        if extrato:
            for movimento in extrato:
                print(movimento)
            print(f"Saldo atual: R${saldo:.2f}")
        else:
            print("Não há movimentações no extrato")

    elif opcao == "0":
        print("Saindo...")
        break

    else:
        print("Operação inválida. Por favor, selecione novamente a operação desejada.")
