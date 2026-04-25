def cadastrar_lote(nome):
    with open("lotes.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"Lote registrado: {nome}\n")
    print(" -- Lote salvo com sucesso -- ")

def exibir_lotes():
    with open("lotes.txt", "r", encoding="utf-8") as arquivo:
        print(arquivo.read())
    print(" -------------------------- ")

# 3 FUNÇÃO:

def resetar_sistema():

    with open("lotes.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write("--- INICIO DE UM NOVO DIA ---\n")
    print(" --- SISTEMA RESETADO COM SUCESSO! --- ")


# PROGRAMA PRINCIPAL

while True:
    print("\nOpções de Sistema:")
    print("1 - Cadastrar Novo Lote")
    print("2 - Exibir Lotes Cadastrados")
    print("3 - Resetar Arquivo (Limpar tudo)")
    print("0 - Desligar Sistema.")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome_lote = input("Digite o código do Lote: ")
        cadastrar_lote(nome_lote)
    elif opcao == "2":
        exibir_lotes()
    elif opcao == "3":
        resetar_sistema()
    elif opcao == "0":
        print("Encerrando o sistema (encerrando as operações...)")
        break
    else:
        print("Opcção invalida! Tente novamente.")