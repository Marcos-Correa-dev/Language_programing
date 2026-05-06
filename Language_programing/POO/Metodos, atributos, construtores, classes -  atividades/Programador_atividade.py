""""
"""""

class Programador:

    # Construtor
    def __init__(self, nome, linguagem):
        self.nome = nome
        self.linguagem = linguagem
        self.produtividade = 100

    #metodo 1
    def codificar(self, horas):
        perda_energia = horas * 5
        self.produtividade -= perda_energia
        print(f"{self.nome} programou em {self.linguagem} por {horas} horas.")

    #metodo 2
    def tomar_cafe(self):
        self.produtividade += 15
        print(f"Café tomado! a produtividade de {self.nome} subiu!!!!")

    #metodo 3

    def verificar_produtividade(self):
        # Apenas retorna o valor, quem imprime é o programa principal
        return self.produtividade


dev = Programador("Peterson", "JavaScript")

dev.codificar(4) # Trabalhou 4 horas (perde 20)
nivel_atual = dev.verificar_produtividade()
print(f"Produtividade após o código: {nivel_atual}")


dev.tomar_cafe()  # Ganha 15
nivel_atual = dev.verificar_produtividade()
print(f"Produtividade após o café: {nivel_atual}")