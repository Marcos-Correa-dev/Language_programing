'''''Antes de escrever o código, crie um diretório chamado Projeto_Bruxo. Todo o seu projeto deverá ser salvo dentro desta pasta.
Passo 2: Os Arquivos do Sistema
Dentro do diretório, construa os dois arquivos abaixo:
1. Módulo mutacoes.py (Regras Fisiológicas e Segurança):
Crie uma classe chamada Witcher.
O construtor (__init__) recebe o nome do bruxo (Atributo Público).
A classe deve possuir dois atributos ESTRITAMENTE PRIVADOS: __toxicidade_atual (inicia em 0) e __limite_toxico (inicia em 100).
Método PROTEGIDO _checar_overdose(aumento_toxico): Este método será a trava de segurança. Crie uma lógica que some a __toxicidade_atual com o aumento_toxico. Se o resultado for maior que o __limite_toxico, retorne False (Risco de morte). Caso contrário, retorne True (Seguro beber).
Método beber_pocao(nome_pocao, nivel_toxico): * Na primeira linha, chame o método _checar_overdose(nivel_toxico).
Se a resposta for False, levante (raise) um ValueError com a mensagem: "Toxicidade Letal Atingida! O bruxo não suporta esta poção."
Se for True, some o nivel_toxico à __toxicidade_atual e retorne uma mensagem de sucesso.
Método meditar(): Este método deve simplesmente zerar (0) a __toxicidade_atual e imprimir que o sangue do bruxo foi purificado.
2. Arquivo principal jornada.py (A Interface de Batalha):
Importe a classe Witcher do módulo mutacoes.py.
Instancie o objeto do bruxo passando o nome (ex: "Geralt").
Crie um menu em loop (while True) com as opções: 1 - Beber Poção, 2 - Meditar, 3 - Ver Status Sanguíneo, 0 - Sair.
Tratamento de Exceções: Na opção 1, peça o nome da poção (texto) e o nível'''''
class Witcher:
    def __init__(self,nome_bruxo,toxidade_atual,limite_toxidade):
        self.nome_bruxo=nome_bruxo
        self.__toxidade_atual =toxidade_atual
        self.__limite_toxidade=limite_toxidade
        self.__toxidade_atual=0
        self.__limite_toxidade =100

    def _checar_overdose(self,aumento_toxico):
        if (self.__toxidade_atual + aumento_toxico )> self.__limite_toxidade :
            return False
        return True

    def beber_porcao(self,nome_porcao, nivel_toxico):
        if not self._checar_overdose(nivel_toxico):
            raise ValueError(f"Toxidade letal {nome_porcao}")
        self.__toxidade_atual += nivel_toxico
        return f"porção {nome_porcao} connsumido "


    def meditar(self):
        self.__toxidade_atual = 0
        return f"meditação concluida .Sangue purificado "
    def ver_status(self):
        return self.__toxidade_atual
