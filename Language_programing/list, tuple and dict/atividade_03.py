funcionario = [
    {"nome": "Ana", "cargo": "Desenvolvedora", "salario": 4500.00},
    {"nome": "Joao", "cargo": "Suporte", "salario": 2500.00},
    {"nome": "Jose", "cargo": "Analista", "salario": 3900.00}
]

for func in funcionario:
    if func["salario"] < 4000:
        aumento =func["salario"] * 0.10
        func["salario"] += aumento
        print(f"Aumento salario para: {func['nome']}")
print("\n-- RELATÓRIO FINAL : ---")

for func in funcionario:
    print(f"Funcionario: {func['nome']} | Novo salário atualizado: {func['salario']}")