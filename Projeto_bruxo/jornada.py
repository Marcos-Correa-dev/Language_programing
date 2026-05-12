'''''2. Arquivo principal jornada.py (A Interface de Batalha):
Importe a classe Witcher do módulo mutacoes.py.
Instancie o objeto do bruxo passando o nome (ex: "Geralt").
Crie um menu em loop (while True) com as opções: 1 - Beber Poção, 2 - Meditar, 3 - Ver Status Sanguíneo, 0 - Sair.
Tratamento de Exceções: Na opção 1, peça o nome da poção (texto) e o nível'''''''''

from mutacoes import Witcher

lobo_branco = Witcher("geralt de rivia")
while True:
    print("1 - Beber Poção")
    print("2 - Meditar ")
    print("3 - ver status Sanguineo")
    print("0 - Sair")

    opcao=input("Escolha opção  ")

    if opcao == "1":
        try:
            nome_p = input("Digite o nome da porção ")
            toxico= int(input("Nivel de toxidade"))
            msg = lobo_branco.beber_pocao(nome_p,toxico)
            print(f"{msg}")
        except ValueError as e:
            print(f"Erro GRAVE: {e}")
    elif opcao == "2":
        print(lobo_branco.meditar())
    elif opcao == "3":
        print(f"Nivel toxico {lobo_branco._checar_overdose(0)}/100")
        break





