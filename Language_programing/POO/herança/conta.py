class Conta:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo
    def info_conta(self):
        print(f"Titular: {self.titular} | Saldo: R$ {self.saldo:.2f}")

# Subclasse (Classe Filha) - herança

class ContaPoupanca(Conta):
    def __init__(self, titular, saldo, taxa_rendimento):
        # O super() chama o __init__ da classe Mãe(conta)
        # Assim, não precisamos de reescrever self.titular = titular, etc.
        super().__init__(titular, saldo)

        # atributo da classe filho:
        self.taxa_rendimento = taxa_rendimento

     #metodo exclusivo da classe filho
    def render_juros(self):
        rendimento = self.saldo * self.taxa_rendimento
        self.saldo += rendimento
        print(f"Rendimento de R${rendimento:.2f} aplicado!")

print("SISTEAM BANCÁRIO: HERANÇA")
#Criando a conta poupança
minha_poupanca = (ContaPoupanca
                  ("Jose",
                   100000,
                   0.05))

# Ela herdou o método info_conta da classe mãe!
minha_poupanca.info_conta()

# Usando o metódo que só a classe filha tem
minha_poupanca.render_juros()

#verificando o novo saldo:
minha_poupanca.info_conta()
