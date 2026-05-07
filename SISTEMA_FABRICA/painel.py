from SISTEMA_FABRICA.maquinas import Esteira

print("=== CONFIGURAÇÃO DO CHÃO DE FÁBRICA ====")

# Fazendo com input:
tag_digitada = input("Digite a TAG da nova Esteira: ")
vel_maxima = int(input("Qual a velocidade máxima dessa esteira?"))

# CRIANDO NOSSO OBJETO COM OS DADOS QUE FORNECEMOS
minha_esteira = Esteira(tag_digitada, vel_maxima)
print(f"\nEsteira {minha_esteira.codigo_tag} instalada com sucesso! ")


# PROGRAMA PRINCIPAL - UTILIZANDO O WHILE TRUE

while True:
    print("\n--- Painel do Operador ---")
    print("1 - Ligar Esteira")
    print("2 - Ajustar Velocidade")
    print("3 -  Desligar Esteira")
    print("0 -  SAIR")

    opcao = input("Escolha uma ação: ")

    if opcao == "1":
        senha = input("Digite a senha do operador:")
        # Chamando o metodo herdado da classe Máquina!
        minha_esteira.ligar(senha)

    elif opcao == "2":

        nova_vel = int(input("Digite a nova velocidade desejada: "))
        # Chamando o metodo exclusivo da  classe filho: Esteira!
        minha_esteira.ajustar_velocidade(nova_vel)

    elif opcao == "3":
        # chamando o metodo herdado da classe mãe (desligar)
        minha_esteira.desligar()

    elif opcao == "0":
        print("Encerrando o painel...")
        break
    else:
        print("Opção invalida!")
