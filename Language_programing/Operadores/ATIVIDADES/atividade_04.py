# atividade 04 - nota  minima 7.0

media = float(input("Digite a média do aluno: "))
presenca = int(input("DIgite a porcentagem de presença: "))

# Avaliando a lógica no script abaixo:
# Regra a (Media e Presença) ou Regra b (Genio = 10 pontos)

aprovado = (media >= 7.0 and presenca >= 75) or (media == 10.0)

print(f"Aluno Aprovado: {aprovado}")


print("Fim do programa")