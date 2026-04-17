idade = int(input("Qual a sua idade? "))
# 19
pulseira = int(input("Tem pulseira vip? (1 Para sim, 0 para Não)"))
# 0
acesso  = idade >= 19 and pulseira == 1

#

print(f"Acesso Liberado: {acesso}")