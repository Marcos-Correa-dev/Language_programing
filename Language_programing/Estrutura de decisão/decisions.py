# # Definindo variável
#
# idade = 20
#
# # Estrutura básica de decisão
#
# if idade >= 18:
#     print("Você é maior de idade! ")
# elif 13 <= idade < 10:
#     print("Você é adolescente! ")
# else:
#     print("Você é menor de idade! ")

# Atividade: faça com estruturas condicionais.
# um sistema que receberá uma variável idade e
# tem_carteira?
# irão ter que colcoar if, else para validar se o
# usuario pode dirigir ou não!

idade = 17
tem_carteira = True

if idade >= 18:
    if tem_carteira:
        print("Você pode dirigir. ")
    else:
        print("Você não pode dirigir, sem carteira.")
else:
    print("Você é menor de idade e não pode dirigir. ")

