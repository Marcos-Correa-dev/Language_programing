class Funcionario:
    taxa_bonus = 0.10
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario

    def calcular_bonus(self):
        # O self acede o salário do próprio objeto e multiplica pela taxa da classe
        return self.salario * Funcionario.taxa_bonus


# criando objetos

func1 = Funcionario("Ana Silva", "Gerente", 20000.00)

func2 = Funcionario("Carlos mendes", "Atendente", 1500.00)


# chamando e calculando e exibindo o bonus de cada um

bonus_ana = func1.calcular_bonus()
bonus_carlos = func2.calcular_bonus()

print(f"O Funcionario {func1.nome} ({func1.cargo}) tem um bonus de: {bonus_ana}")

print(f"O Funcionario {func2.nome} ({func2.cargo}) tem um bonus de: {bonus_carlos}")
