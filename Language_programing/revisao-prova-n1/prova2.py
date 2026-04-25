# 1. FUNÇÃO: O Cuidadoso (Modo 'x' - Cria mas dá erro se já existir)
def criar_arquivo_mestre(nome_fabrica):
    with open("mestre.txt", "x", encoding="utf-8") as arquivo:
        arquivo.write(f"=== CONFIGURAÇÃO: {nome_fabrica} ===\n")
        arquivo.write("Lista de Operadores Autorizados:\n")
    print(">> ALERTA: Arquivo mestre gerado com segurança!\n")


# 2. FUNÇÃO: Adicionar sem sobrescrever (Modo 'a')
def adicionar_operador(nome):
    with open("mestre.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"- Operador: {nome}\n")
    print(">> Operador registrado com sucesso!\n")


# 3. FUNÇÃO: Apenas Leitura (Modo 'r')
def ler_arquivo():
    print("\n--- LENDO DADOS DO SERVIDOR ---")
    with open("mestre.txt", "r", encoding="utf-8") as arquivo:
        conteudo = arquivo.read()
        print(conteudo)
    print("-------------------------------")


# --- PROGRAMA PRINCIPAL ---
print("--- SISTEMA DE SEGURANÇA MÁXIMA ---")

# 4. Laço infinito do Menu
while True:
    print("\nMenu de Acesso:")
    print("1 - Gerar Arquivo Mestre (Atenção: Use apenas 1 vez!)")
    print("2 - Adicionar Operador")
    print("3 - Ler Arquivo")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    # 5. Condições e chamadas de função
    if opcao == "1":
        fabrica = input("Digite o nome da sua Fábrica: ")
        criar_arquivo_mestre(fabrica)

    elif opcao == "2":
        operador = input("Digite o nome do operador: ")
        adicionar_operador(operador)

    elif opcao == "3":
        ler_arquivo()

    elif opcao == "0":
        print("Desligando o terminal...")
        break

    else:
        print("Opção inválida!")