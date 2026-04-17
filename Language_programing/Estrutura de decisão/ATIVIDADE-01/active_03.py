while True:
    print("-------MENU PRINCIPAL-------")
    print("1 - Iniciar Máquina")
    print("2 - Desligar Máquina")
    print("0 - Sair do Sistema")
    opcao = int(input("Escolha a Opção: "))
    if opcao == 1:
        print("Máquina Rodando!!!")
    elif opcao == 2:
        print("Máquina Parando!!!")
    elif opcao == 0:
        print("Encerrando o Software!!!")
        break
    else:
        print("Opção Inválida!!!")