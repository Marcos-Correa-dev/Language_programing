class Personagem:
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = int(vida)

    def atacar(self, defensor, dano):
        print(f"{self.nome} atacou {defensor.nome}")

        defensor.vida -= dano

        print(f"{defensor.nome} sofreu {dano} de dano. Vida restante: {defensor.vida}")

class Heroi(Personagem):
    def __init__(self, nome, vida, habilidade):
        super().__init__(nome, vida)
        self.habilidade = habilidade

class Vilao(Personagem):
    def __init__(self, nome, vida, poder):
        super().__init__(nome, vida)
        self.poder = poder


superman = Heroi("Superman", 100, "Visão de calor")
lex_luthor = Vilao("Lex Luthor", 80, "Inteligência")

print("==========INICIO DA BATALHA=============")
print(f"{superman.nome} (vida: {superman.vida}) VS {lex_luthor.nome} (vida: {lex_luthor.vida}) ")

# O superman (self) chama o método e ataca o lex luthor
superman.atacar(lex_luthor, 20)

# O lex chama (self) Herda o MESMO METODO para revidar
lex_luthor.atacar(superman, 40)

superman.atacar(lex_luthor, 60)


