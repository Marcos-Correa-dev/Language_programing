
from Language_programing.Tratamento_de_exceção.Arquivos.funcionario import Funcionario

print("=======SISTEMA DE FOLHA DE PAGAMENTO =======")

lista_Funcionario = []

while True:
    print("\n--- Novo Cadastro ---")
    nome_input = input("Nome do Funcionario: (ou 'sair' para encerrar):" )

    if nome_input.lower() == 'sair':
        break

    try:
        salario_input = float(input("Digite o salário: R$"))

        if salario_input < 0:
            raise ValueError("O salário não pode ser negativo")

    except ValueError as erro:

        print(f"Erro de digitação: O valor inserio é invalido. Tente novamente.")
        print(f"Detalhe técnico: {erro}")
        continue

    novo_funcionario = Funcionario(nome_input, salario_input)
    lista_Funcionario.append(novo_funcionario)
    print(f"{nome_input} cadastrado com sucesso!")

print("\n=== RESUMO DA FOLHA DE PAGAMENTO ===")
total_folha = 0

for func in lista_Funcionario:

    total_folha += func.calcular_salario()
    print(f"Colaborador: {func.get_nome()} | Salário: R${func.calcular_salario()}")

print("-"*40)
print(f"TOTAL A PAGAR PELA EMPRESA: {total_folha:.2f}")