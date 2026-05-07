class ContaBancaria:
    def __init__(self, titular, cpf, senha, saldo_inicial):
        # 1. PÚBLICO: Acesso livre de qualquer lugar
        self.titular = titular

        # 2. PROTEGIDO: Convenção para "não mexa fora da classe ou subclasses"
        self._cpf = cpf

        # 3. PRIVADO: O Python dificulta o acesso direto (Name Mangling)
        self.__senha = senha
        self.__saldo = saldo_inicial

    def mostrar_dados(self):
        # Dentro da classe, temos acesso a tudo livremente
        print(f"Titular: {self.titular}")
        print(f"CPF: {self._cpf}")
        print(f"Saldo: R$ {self.__saldo}")


# --- TESTANDO OS ACESSOS ---
minha_conta = ContaBancaria("Marcos", "123.456.789-00", "1234", 1000)

print("=== TESTE DE ACESSO EXTERNO ===")

# ACESSO AO PÚBLICO: Funciona perfeitamente
print(f"Nome do Titular: {minha_conta.titular}")

# ACESSO AO PROTEGIDO: Funciona (o Python permite), mas é má prática
# O sublinhado avisa: "Sou um detalhe interno, evite me acessar aqui!"
print(f"CPF (Protegido): {minha_conta._cpf}")

# ACESSO AO PRIVADO: Vai gerar um ERRO (AttributeError)
# O Python "escondeu" este atributo para proteger o dado
try:
    print(minha_conta.__saldo)
except AttributeError:
    print("ERRO: Não é possível acessar o saldo diretamente! Ele é PRIVADO.")