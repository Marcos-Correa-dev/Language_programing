class PlayerMusical:
    # construtor
    def __init__(self):
        self.volume = 50
        self.tocando = False # Nasce pausado

    # método 1

    def play(self):
        if self.tocando == False:
            self.tocando = True
            print(" Música iniciada. ")
        else:
            print("O player já está tocando")


    # metodo
    def pause(self):
        if self.tocando == True:
            self.tocando = False
            print(" Música pausada. ")
        else:
            print("O player já está pausado.")

    #metodo 3

    def aumentar_volume(self, passos):
        self.volume += passos
        if self.volume > 100:
            self.volume = 100

        print(f"Volume atual: {self.volume}")


caixa_De_som = PlayerMusical()
caixa_De_som.play()
caixa_De_som.aumentar_volume(20) # Vai para 70
caixa_De_som.aumentar_volume(50) # Iria para 120 , mas o IF trava no 100!!!!!
caixa_De_som.pause()