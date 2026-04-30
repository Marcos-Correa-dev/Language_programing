# Criando uma classe chamada ContaBancaria

class ContaBancaria:
    # Atributo de classe
    taxa_manutencao = 15.0

    def __init__(self, titular, saldo=0):
        # Atributos de instância/Referência (Cada um tem o seu)
        self.titular1 = titular   # atributo de referência
        self.saldo1 = saldo   # Atributo de referência

    # Metodo 1: Depositar
    def depositar(self, quantia):
        self.saldo1 += quantia  # atributo de referência
        print(f"Depósito de R$: {quantia} realizado. Novo Saldo: R$ {self.saldo1}")

     # Metodo 2: Sacar (Com lógica de programação)
    def sacar(self, quantia):
        # O self "self" é obrigatorio para acessar o saldo do próprio objeto!
        if quantia <= self.saldo1:
            self.saldo1 -= quantia

            print(f"Saque de R$: {quantia} autorizado!")
        else:
            print(f"Saque Negado para: {self.titular1}. Saldo insuficiênte.")
            return False


conta_alexandre = ContaBancaria("Alexandre Mendes", 100)
conta_aluno = ContaBancaria("Aluno-E-Tech", 70)

# Mostrando os métodos
conta_alexandre.depositar(50) # Saldo vai para 150
conta_alexandre.sacar(200)  # o If vai bloquear! (150 < 200)
conta_aluno.sacar(20)  # o if vai permitir (50 >20)


print(f"Taxa do banco para todas as contas: R$ {ContaBancaria.taxa_manutencao}")

