# def gerar_etiqueta_diaria(lote, produto):
#     # O modo 'W' cria o arquivo
#     with open("etiqueta_producao.txt", "w", encoding="utf-8") as arquivo:
#         arquivo.write("==Etiqueta do dia==\n")
#         arquivo.write(f"Lote: {lote}\n")
#         arquivo.write(f"Produto: {produto}\n")
#     print("-- Etiqueta nova gerada com sucesso! --")
# gerar_etiqueta_diaria("L-998", "Placa Mãe tuf gamer")


# O modo 'a' (append - nesse caso o 'a' irá deixar histórico)

# def registrar_carminhao(placa):
#     #O modo 'a' abre o arquivo e joga a caneta lá para a ultima linha.
#     with open("registro_portaria.txt", "a", encoding="utf-8") as arquivo:
#         arquivo.write(f"Caminhão placa: {placa} liberado para entrada.\n")
#     print(f" -- Caminhão {placa} salvo no histórico! ---")
#
#
# registrar_carminhao("ABC-1234")
# registrar_carminhao("KJX-8B39")


# """"
#     O modo 'r' (Read - Leitura)
# """""
from email.encoders import encode_noop

# def ler_relatorio_portario():
#     print("\n --- Lendo RELATÓRIO PORTARIA ---")
#     # o MODO 'r' só serve para ler.
#     with open("registro_portaria.txt", "r", encoding="utf-8") as arquivo:
#         texto = arquivo.read()
#         print(texto)
# ler_relatorio_portario()

# """
#     O modo 'x' (Exclusivo de criação)
# """""

# def criar_configuracao_inicial():
#     # O modo 'x' cria o arquivo, mas se ELE JÁ EXISTIR , o python dá erro.
#     # Para garantir que não vamos sobreescrever um arquivo importante.
#     with open("configuracao_sistema.txt", "x", encoding="utf-8") as arquivo:
#         arquivo.write("TEMA=Escuro\nIDIOMA=PT-BR")
#     print(" -- Arquivo de configuração criado com sucesso! -- ")
#
# criar_configuracao_inicial()


# O modo binario 'b'

def fazer_backup_imagem():
    # 'rb' = Read Binary (ler dados brutas da imagem binario)
    with open("logo.png", "rb") as arquivo_original:
        dados_da_foto = arquivo_original.read()
    # 'w' Write Binary (escreve os dados brutos num arquivo
    with open("Logo_backup.png", "wb") as arquivo_novo:
        arquivo_novo.write(dados_da_foto)

    print(" -- Cópia de segurança da imagem feita com sucesso! -- ")

fazer_backup_imagem()
