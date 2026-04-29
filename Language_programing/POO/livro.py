# class Livro:
#
#     # O __init__ é chamado automaticamente na hora da criação
#     def __init__(self, titulo_dado, autor_dado):
#         # O 'self' diz: " O titulo DESTE objeto é igual ao titulo_dado
#         self.titulo = titulo_dado
#         self.autor = autor_dado
#         print(f"O Livro '{self.titulo}' do autor {self.autor} acabou de ser criado")
#
#     def exibir_dados(self):
#
#         # O self neste ponto é usado para 'acender'  as variáveis que pertencem à classe
#         print(f" -- Lendo o Livro: {self.titulo}")
#
#
# # Pedindo para o Python construir minha classe com meus objetos:
#
# livro1 = Livro("Python para Iniciantes", "Marcos Corrêa")
# livro2 = Livro("Lógica Avançada", "Ada Lovelace")
#
# livro1.exibir_dados()
# livro2.exibir_dados()

class Funcionario:
    def __init__(self, nome, cargo):
        self.nome1 = nome
        self.cargo1 = cargo

    def exibir_dados(self):
        # Aqui estarei retornando/exibindo o valor para o utilziador
        print(f"Colaborador: {self.nome1} | Cargo: {self.cargo1}")

# Criando as instâncias (OS OBJETOS REAIS)
funcionario1 = Funcionario("João Silva", "Tecnico de Automação")
funcionario2 = Funcionario("Ana Costa", "Engenheira de Dados")


funcionario1.exibir_dados()
funcionario2.exibir_dados()