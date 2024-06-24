menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Cadastrar Usuário
[5] Cadastrar Conta
[6] Procurar Conta por CPF
[0] Sair

=> """

contas = []
AGENCIA = "0001"
LIMITE_SAQUES = 3

def depositar(conta, valor):
    if valor > 0:
        conta['saldo'] += valor
        conta['extrato'].append(f"Depósito: R${valor:.2f}")
        print(f"Depósito de R${valor:.2f} realizado com sucesso!")
    else:
        print("Valor de depósito inválido.")

def sacar(conta, valor):
    if conta['numero_saques'] < LIMITE_SAQUES:
        if valor > 0:
            if valor <= conta['saldo'] and valor <= conta['limite']:
                conta['saldo'] -= valor
                conta['extrato'].append(f"Saque: R${valor:.2f}")
                conta['numero_saques'] += 1
                print(f"Saque de R${valor:.2f} realizado com sucesso!")
            elif valor > conta['limite']:
                print(f"Valor excede o limite de saque de R${conta['limite']:.2f}")
            else:
                print("Saldo insuficiente.")
        else:
            print("Valor de saque inválido.")
    else:
        print("Limite de saques diários atingido.")

def exibir_extrato(conta):
    print("Extrato")
    if conta['extrato']:
        for movimento in conta['extrato']:
            print(movimento)
    else:
        print("Não há movimentações.")
    print(f"Saldo atual: R${conta['saldo']:.2f}")

def cadastrar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    if any(usuario['cpf'] == cpf for usuario in usuarios):
        print("Já existe um usuário com esse CPF!")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
    
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("Usuário cadastrado com sucesso!")

def cadastrar_conta(contas, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = next((usuario for usuario in usuarios if usuario['cpf'] == cpf), None)
    
    if usuario:
        numero_conta = len(contas) + 1
        contas.append({
            "agencia": AGENCIA, 
            "numero_conta": numero_conta, 
            "usuario": usuario, 
            "saldo": 0, 
            "limite": 500, 
            "extrato": [], 
            "numero_saques": 0
        })
        print(f"Conta número {numero_conta}, Agência {AGENCIA} cadastrada para o usuário {usuario['nome']}.")
    else:
        print("Usuário não encontrado. Cadastro de conta não realizado.")

def selecionar_conta(contas):
    agencia = input("Informe o número da agência: ")
    numero_conta = int(input("Informe o número da conta: "))
    conta = next((conta for conta in contas if conta['agencia'] == agencia and conta['numero_conta'] == numero_conta), None)
    
    if conta:
        return conta
    else:
        print("Conta não encontrada.")
        return None

def procurar_conta_por_cpf(contas):
    cpf = input("Informe o CPF do usuário: ")
    contas_usuario = [conta for conta in contas if conta['usuario']['cpf'] == cpf]
    
    if contas_usuario:
        print(f"Usuário com CPF {cpf} possui as seguintes contas:")
        for conta in contas_usuario:
            print(f"Agência: {conta['agencia']}, Conta: {conta['numero_conta']}")
    else:
        print("Nenhuma conta encontrada para o CPF informado.")

usuarios = []

while True:
    opcao = input(menu)
    print(f"Opção escolhida: {opcao}")

    if opcao == "1":
        conta = selecionar_conta(contas)
        if conta:
            try:
                valor_deposito = float(input("Valor do depósito: "))
                depositar(conta, valor_deposito)
            except ValueError:
                print("Entrada inválida, por favor insira um número.")

    elif opcao == "2":
        conta = selecionar_conta(contas)
        if conta:
            try:
                valor_saque = float(input("Valor do saque: "))
                sacar(conta, valor_saque)
            except ValueError:
                print("Entrada inválida, por favor insira um número.")

    elif opcao == "3":
        conta = selecionar_conta(contas)
        if conta:
            exibir_extrato(conta)

    elif opcao == "4":
        cadastrar_usuario(usuarios)

    elif opcao == "5":
        cadastrar_conta(contas, usuarios)

    elif opcao == "6":
        procurar_conta_por_cpf(contas)

    elif opcao == "0":
        print("Saindo...")
        break

    else:
        print("Operação inválida. Por favor, selecione novamente a operação desejada.")
