# Registre um pedido no fim do arquivo de log.
def salvar_pedido(numero_pedido, cliente, valor):
    with open("pedidos_vendas.txt", "a", encoding="utf-8") as arquivo:

        linha = f"Pedido #{numero_pedido} | Cliente: {cliente} | Valor: R$ {valor:.2f}\n"
        arquivo.write(linha)
    print(" -- O pedido foi gravado com sucesso! -- ")

def exibir_pedidos():

    print("\n ---- HISTÓRICO DE VENDAS/PEDIDOS -----")
    with open("pedidos_vendas.txt", "r", encoding="utf-8") as arquivo:
        conteudo = arquivo.read()
        print(conteudo)
    print("====== sucesso ===== ")


    # ESTRUTURA PRINCIPAL (MENU DE SISTEMA)

    print("Bem-vindo ao Sistema de Vendas!")

while True:
    print("\n1 - Cadastrar Novo Pedido ")
    print("2 - Exibir Todos os Pedidos ")
    print("0 - Desligar Sistema")

    opcao = input("O que deseja fazer?")

    if opcao == "1":
        numero = int(input("Digite o número do pedido: "))
        nome = input("Digite o nome do Cliente: ")
        valor_compra = float(input("Digite o valor da compra total: R$ "))

        salvar_pedido(numero, nome, valor_compra)

    elif opcao == "2":
        # Chamando a função de leitura
        exibir_pedidos()
    elif opcao == "0":
        print("Salvando dados e encerrando... até logo!")
        break
    else:
        print("Opção invalida! Digite 1, 2 ou 0")