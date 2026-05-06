class ContaSegura:
    def __init__(self, titular, senha, saldo_inicial=0):
        self.titular = titular

        # '__' transforma o saldo num ATRIBUTO PRIVADO
        self.__saldo = saldo_inicial
        self.__senha = senha

    def depositar(self, quantia):
        if quantia > 0:
            self.__saldo += quantia
            print(f"Deposito de R$: {quantia} efetuado!")
        else:
            print("Valor invalido para o depósito.")

    # Regra de negocio: não deixa sacar se não tiver dinheiro
    def sacar(self, senha_tentativa, quantia):
        # primeiro nivel de segurança: valida se a senha ta correta
        if senha_tentativa == self.__senha:
            if quantia <= self.__saldo:
                print(f"Saque de R$: {quantia} autorizado!")
                return True
            else:
                print(f"Saque Negado: Saldo insuficiente.")
                return False
        else:
            print("Saque Negado: Senha incorreta!")
            return False

    def trocar_senha(self, senha_atual, nova_senha):
        if senha_atual == self.__senha:
            self.__senha = nova_senha
            print("Sucesso! Senha alterada com sucesso!")
        else:
            print("Saque Negado: Senha incorreta!")
            return False


    def get_saldo(self, senha_tentativa):
        if senha_tentativa == self.__senha:
            return f"R$ {self.__saldo}"
        else:
            return "Acesso Negado (Senha incorreta)."

print("SISTEMA BANCÁRIO")

conta_segura = ContaSegura("Joao", "1234", 5000)

# chamando a conta da forma correta (através de métodos)
conta_segura.depositar(1000) # vai para 6000
#tentativa com senha errada
conta_segura.sacar("000", 500)

conta_segura.sacar("1234", 600)
conta_segura.trocar_senha("0000", "6789")
print("TENTATIVA DE FRAUDE")

conta_segura.__saldo = 99999999

print(f"Saldo após tentativa de fraude: R$ {conta_segura.get_saldo('999')}")