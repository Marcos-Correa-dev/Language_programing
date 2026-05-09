class PacoteBase:
    def __init__(self, origem, data_hora):
        self.origem = origem
        self.data_hora = data_hora

    def processar(self):
        print("Processando pacote genérico")

class PacoteAlarme(PacoteBase):
    def __init__(self, origem, data_hora, gravidade):
        # Chama o construtor da classe mãe
        super().__init__(origem, data_hora)
        self.gravidade = gravidade

    def processar(self):
        # polimorfismo:
        if self.gravidade.upper() == "ALTA":
            print(f"[{self.data_hora}] ALERTA CRÍTICO: FALHA NA {self.origem.upper()}! (GRAVIDADE ALTA)")
        else:
            print(f"[{self.data_hora}] Aovis: Alarme de gravidade {self.gravidade} na {self.origem}")

class PacoteProducao(PacoteBase):
    def __init__(self, origem, data_hora, quantidade_pecas):
        # chama o construtor da classe mãe
        super().__init__(origem, data_hora)
        self.quantidade_pecas = quantidade_pecas

    def processar(self):
        #polimorfismo:
        print(f"[{self.data_hora}] SUCESSO: foram salvas {self.quantidade_pecas}")