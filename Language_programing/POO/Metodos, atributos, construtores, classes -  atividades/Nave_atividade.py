class Nave:

    def __init__(self, nome, combustivel):
        self.nome = nome
        self.combustivel = combustivel
        self.status = "Estacionada" # Atributo de estado padrão

    def decolar(self):
        if self.combustivel >= 20:
            self.combustivel -= 20
            self.status = "Em voo"
            print(f" Decolagem Autoizada! a Nave {self.nome} está no espaço! ")
        else:
            print("Combustível insuficiente!")

    def recarregar(self, quantidade):
        self.combustivel += quantidade
        print(f" -- Abastecimento concluído, Nível atual {self.combustivel} unidades. ")

    def verificar_status(self):
        print(f" --------- PAINEL DA NAVE -------- ")
        print(f"Nave: {self.nome} | Status: {self.status}")
        print(f" ---------------- ")


# Area de testes

minha_nave = Nave("Apollo", 15)
minha_nave.verificar_status()

minha_nave.decolar() # vai dar erro de combustivel
minha_nave.recarregar(10)
minha_nave.decolar() # agora vai voar!
minha_nave.verificar_status()