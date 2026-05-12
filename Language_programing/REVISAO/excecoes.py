# print("------ Teste de aptidão Jedi ---")
#
#
# try:
#     nivel_forca = int(input("Jovem Padwan, digite o seu nível de Força (1 a 10)"))
#     print(f"Mestre Obi-wan: Muito bem, o seu nível é {nivel_forca}.")
#
# except ValueError:
#     print("Mestre Yoda: Letras você digitou. Números usar você deve!")
#
# print("Teste encerrado.")


# print("--- DIVISÂO DE RAÇÕES ÉLFICAS ---")
#
# try:
#     pao = 20
#     membros_socidade = int(input("Quantos membros ainda restam na "
#                                  "Sociade dos Anões?"))
#
#     # Poderia dar erro se membros_sociedade for ZERO
#     porcao = pao / membros_socidade
#     print(f"Aragon: Cada membro receberá {porcao} pedaços de pão...")
#
# except ValueError:
#     print("Gandalf: Fale a quantidade em números, seu tolo!")
#
# except ZeroDivisionError:
#     print("Gimli: Zero membros? Então não sobrou ninguém vivo? "
#           "mais pão para mim!")


#
# def diagnosticar_armadura():
#     print("Sexta-Feira: Iniciando diagnóstico de reator Arc...")
#
#     try:
#         energia = int(input("Tony, insira a voltagem atual do reator: "))
#         teste = 1000 / energia
#
#     except ValueError:
#         print("Sexta-feira: O sensor falhou. Recebi texto em vez de números...")
#
#     except ZeroDivisionError:
#         print("Sexta-feira: Alerta critico, Reator zerado! Risco de morte iminente")
#
#     else:
#         # Só roda se o "try" for um SUCESSO ABSOLUTO(sem nenhum erro)
#         print("Sexta-feira: Diagnostico Perfeito. Armadura 100% pronta para combate!", teste)
#
#     finally:
#         # Ele sempre rodará no final. dando certo ou errado!
#         print("Sexta-feira: Fechando painéis de diagnostico do peito.")
#
# diagnosticar_armadura()

"""""Antes de escrever o código, crie um diretório chamado Projeto_Bruxo. Todo o seu projeto deverá ser salvo dentro desta pasta.
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
Tratamento de Exceções: Na opção 1, peça o nome da poção (texto) e o nível tóxico dela (número inteiro). Envolva essa rotina num bloco try/except. Capture o ValueError para proteger o sistema caso o usuário digite letras no lugar do nível tóxico ou caso a classe avise que o limite letal foi atingido. Imprima a mensagem de erro formatada.
"""""

