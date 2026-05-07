class Maquina:
    def __init__(self, codigo_tag):
        self.codigo_tag = codigo_tag

        # Encapsulamento
        self.__ativa = False

    # Nosso metodo seguro: (exige senha)
    def ligar(self, senha_operador):
        if senha_operador == "1234":
            self.__ativa = True
            print(f"\n[SISTEMA] Máquina {self.codigo_tag} LIGADA.")
        else:
            print("\n[ERRO] Senha incorreta! Máquina bloqueada.")

    #Nosso metodo de desligar
    def desligar(self):
        self.__ativa = False
        print(f"\n[SISTEMA] Máquina {self.codigo_tag} DESLIGADA.")

    #Nosso metodo Getter para outras classes saberem se ela está ligada.
    def is_ativa(self):
        return self.__ativa

class Esteira(Maquina):
    def __init__(self, codigo_tag, velocidade_maxima):
        # Chamando o construtor da classe mãe:
        super().__init__(codigo_tag)

        self.velocidade_maxima = velocidade_maxima
        self.velocidade_atual = 0

    def ajustar_velocidade(self, nova_velocidade):
        #A esteira só pode mudar de velocidade se estiver LIGADA
        if self.is_ativa() == True:
            if nova_velocidade <= self.velocidade_maxima:
                self.velocidade_atual = nova_velocidade
                print(f"[ESTEIRA] {self.codigo_tag} Rodando a {self.velocidade_atual}")
            else:
                print(f"[ALERTA] a velocidade máxima permitida é {self.velocidade_maxima}")
        else:
            print(f"[ERRO] A esteira {self.codigo_tag} está DESLIGADA! Ligue o motor primeiro.")