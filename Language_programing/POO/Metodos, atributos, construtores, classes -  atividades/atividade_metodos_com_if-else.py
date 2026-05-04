class Interruptor:

    # Construtor: usando o init
    def __init__(self):
        self.ligada = False

    # Metodo de ação: (Ligar/desligar)
    def alterar(self):
        # Usando if/else para verificar o estado atual e inverter
        if self.ligada == True:
            self.ligada = False
            print("A luz foi desligada ")

        else:
            self.ligada = True
            print("A luz foi LIGADA!")


meu_interruptor = Interruptor()
print(f"Estado inicial: Ligada = {meu_interruptor.ligada}\n")

meu_interruptor.alterar()  # Estava False, vai para True
meu_interruptor.alterar()  # Estava True, vai para False
meu_interruptor.alterar()  # Estava false, vai ara True

