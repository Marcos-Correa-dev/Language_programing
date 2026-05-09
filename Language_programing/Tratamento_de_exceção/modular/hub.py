
from modular.pacotes import PacoteAlarme, PacoteProducao

fila_de_mensagens = []

print("======== RECEIVE HUB INICIADO =======")

while True:
    print("\n-- MENU ---")
    print("1 - Chegou um Alarme")
    print("2 - Chegou Dados de Produção")
    print("3 - Processar Fila Inteira")
    print("0 - Sair")

    opcao = input("Escolha uma das opções: ")

    if opcao == "1":
        orig = input("Origem: ")
        hora = input("Data/hora: ")
        grav = input("Gravidade (BAIXA, MÉDIDA, ALTA): ")

        # CRIANDO O OBJETO (VARIÁVEL) QUE RECEBE É ADICIONADO NA LISTA
        novo_alarme = PacoteAlarme(orig, hora, grav)
        fila_de_mensagens.append(novo_alarme)
        print(">> Alarme enfileirado com sucesso !")

    elif opcao =="2":
        orig = input("Origem: ")
        hora = input("Data: ")

        try:
            qtd = int(input("Quantidade de peças: (apenas numeros): "))

            nova_producao = PacoteProducao(orig, hora, qtd)
            fila_de_mensagens.append(nova_producao)
            print(">> Dados de produção enfileirados com sucesso!")

        except ValueError:
            print("Erro: Você não digitou um numero inteiro. PACOTE DESCARTADO")


    elif opcao == "3":
        if len(fila_de_mensagens) == 0:
            print("A fila está vazia. Nada para processar")
        else:
            print("\n--- INICIANDO PROCESSO DE FILA ----")

            for pacote in fila_de_mensagens:
                pacote.processar()

            #Lima a fila após processar tudo
            fila_de_mensagens.clear()
            print("--- PROCESSAMENTO CONCLUÍDO ---")


    elif opcao == "0":
        print("ENCERRANDO O RECEIVE HUB")
        break
    else:
        print("opção invalida, tente novamente.")