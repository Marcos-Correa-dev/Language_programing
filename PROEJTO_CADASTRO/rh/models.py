# rh/models.py

from padrao.models import Pessoa

class Funcionario(Pessoa):
    def __init__(self, nome, cpf, cargo, salario):
        # SUPER() chama o construtor da classe mãe
        super().__init__(nome, cpf)

        self.cargo = cargo
        # Atributo privado: Ninguem mexe no salário fora daqui.
        self.__salario = salario


    # Metodo Getter para o financeiro e a
    # contabilidade conseguirem ler o salário.
    def get_salario(self):
        return self.__salario

    def promover(self, novo_cargo, aumento):
        self.cargo = novo_cargo
        self.__salario = aumento
        print(f"\n[RH] Parabéns! {self.nome} foi promovido a {self.cargo}")
