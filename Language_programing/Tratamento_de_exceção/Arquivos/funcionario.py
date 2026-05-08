
class Funcionario:
    def __init__(self, nome, salario):
        #atributos privados
        self.__nome = nome
        self.__salario = salario

    # Metodo para calcular e retornar o salário
    def calcular_salario(self):
        return self.__salario

    def get_nome(self):
        return self.__nome