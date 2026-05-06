class Veiculo:
    def __init__(self, marca, modelo):
        self.marca =marca
        self.modelo = modelo

    def info(self):
        print(f"marca: {self.marca}, Modelo: {self.modelo}")

class Carro(Veiculo):
    def __init__(self, marca, modelo, portas):
        super().__init__(marca, modelo)
        self.portas = portas


meu_veiculo = Veiculo("Marca Genérica", "Modelo Padrão")
print("\nInformação do Veículo Genérico: ")
meu_veiculo.info()


meu_veiculo = Carro("Ford", "mustang", 2)
print("\nInformações do Carro: ")
meu_veiculo.info()