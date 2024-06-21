import csv

class Produto:
    def __init__(self, nome, descricao, valor, disponivel_para_venda):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor
        self.disponivel_para_venda = disponivel_para_venda

    def exibir_detalhes(self):
        return f"{self.nome} - R${self.valor:.2f} - {'Disponível' if self.disponivel_para_venda else 'Indisponível'}"

    def disponibilidade_para_csv(self):
        return 'True' if self.disponivel_para_venda else 'False'

produtos = []

def carregar_produtos():
    try:
        with open('produtos.csv', mode='r', newline='') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                nome, descricao, valor, disponivel = row
                valor = float(valor)
                disponivel_para_venda = disponivel == 'True'
                produtos.append(Produto(nome, descricao, valor, disponivel_para_venda))
    except FileNotFoundError:
        print("Arquivo de produtos não encontrado. Iniciando com lista vazia.")

def salvar_produtos():
    with open('produtos.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Nome', 'Descrição', 'Valor', 'Disponível'])
        for produto in produtos:
            disponivel = produto.disponibilidade_para_csv()
            writer.writerow([produto.nome, produto.descricao, produto.valor, disponivel])

def cadastrar_produto():
    print("\nCadastro de Produto")
    nome = input("Nome do produto: ")
    descricao = input("Descrição do produto: ")
    try:
        valor = float(input("Valor do produto: "))
        if valor >= 0:
            disponivel_para_venda = input("Disponível para venda? (sim/não): ").lower() == 'sim'
            produtos.append(Produto(nome, descricao, valor, disponivel_para_venda))
            print("Produto cadastrado com sucesso!")
            salvar_produtos()  
            listar_produtos()
        else:
            print("O valor do produto não pode ser negativo.")
    except ValueError:
        print("Valor inválido para o preço. Insira um número válido.")


def listar_produtos():
    while True:
        if produtos:
            produtos_ordenados = sorted(produtos, key=lambda produto: produto.valor)
            largura_nome = max(len(produto.nome) for produto in produtos_ordenados) if produtos_ordenados else 0
            largura_valor = max(len(f"R${produto.valor:.2f}") for produto in produtos_ordenados) if produtos_ordenados else 0
            
            print("\nListagem de Produtos")
            print(f"{'Nome':<{largura_nome + 5}} {'Valor':<{largura_valor + 5}}")
            
            for produto in produtos_ordenados:
                disponibilidade = 'Disponível' if produto.disponivel_para_venda else 'Indisponível'
                print(f"{produto.nome:<{largura_nome + 5}} R${produto.valor:.2f} {disponibilidade:<12}")
            
            print("\nOpções:")
            print("[1] Cadastrar novo produto")
            print("[0] Sair")
            opcao = input("=> ")
            
            if opcao == "1":
                cadastrar_produto()
            elif opcao == "0":
                print("Saindo...")
                break 
            else:
                print("Opção inválida. Tente novamente.")
        else:
            print("\nNenhum produto cadastrado.")
            cadastrar_produto()

carregar_produtos()

while True:
    listar_produtos()
    if input("Deseja sair? (s/n): ").lower() == 's':
        print("Saindo...")
        break

#Olá, recrutador! Este progrma foi feito baseado em um curso que participei, onde criei um menu de caixa eletrônico, juntamente com ajuda de uma IA.
#Ainda tenho conhecimentos básicos em programação, não conseguiria fazer este código inteiro sozinha, porém dou um jeito de fazer o que me é pedido, de alguma maneira!
#Espero que o código esteja conforme o que foi solicitado. Agradeço imensamente a oportunidade de participar do processo seletivo, com certeza essa experiência me trouxe mais conhecimento.