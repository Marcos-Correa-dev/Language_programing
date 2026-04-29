"""a o sistema: (Sistema de catálogo de filme) – (0,0 a 4.0)
Crie uma função chamada salvar_filme(titulo, diretor, ano). Essa função deve abrir um arquivo chamado catalogo_filmes.txt no modo de anexar ('a') com encoding="utf-8".
Escreva os dados formatados pulando uma linha no final (Exemplo: "Filme: Matrix | Diretor: Wachowski | Ano: 1999").
Crie uma função chamada listar_filmes(). - done
Ela deve abrir o arquivo catalogo_filmes.txt no modo de leitura ('r') com encoding="utf-8" e imprimir todo o conteúdo na tela.
Crie um laço while True que exiba as opções:
1 - Cadastrar Filme, 2 - Ver Catálogo, e 0 - Sair.
As condições: * Se o usuário digitar 1, crie as variáveis e peça para ele digitar o titulo (String), o diretor (String) e o ano (Inteiro). Em seguida, chame a função salvar_filme passando esses dados.
Se digitar 2, chame a função listar_filmes().
Se digitar 0, use o comando adequado para quebrar o laço e encerrar o programa.
"""""

def salvar_filme(tituto, diretor, ano):
    with open("catalogo_filmes.txt", "a", encoding="utf-8") as arquivo:

        linha = f"Filme: {tituto} | Diretor: {diretor} | ano: {ano}\n"
        arquivo.write(linha)
    print(" --- Sucesso! O filme foi salvo no catalogo! -- ")

def listar_filmes():
    with open("catalogo_filmes.txt", "r", encoding="utf-8") as arquivo:

        conteudo = arquivo.read()
    print(conteudo)


# ---- programa principal

while True:
    print("\n1 Cadastrar Filme")
    print("2 - Ver catalogo")
    print("0 - Sair")

    opcao = input(" O que você deseja fazer?")

    if opcao == "1":
        titulo = input("Digite o titulo do Filme: ")
        diretor = input("Digite o nome do Diretor: ")
        ano = int(input("Digite o ano do lançamento: "))

        # Passando os dados coletados para a minha função
        salvar_filme(titulo, diretor, ano)

    elif opcao == "2":
        listar_filmes()

    elif opcao == "0":
        print("Encerrando o sistema...")
        break
    else:
        print("Opções invalidas: digite( 1, 2 ou 0 )")