valor_conta = float(input("Qual o valor total da conta? "))
amigos = int(input("Quantos amigos vão dividir? "))

gorjeta = valor_conta * 0.10
total_com_gorjeta = valor_conta + gorjeta

valor_por_pessoa = total_com_gorjeta / amigos

print(f"Gorjeta (10%): {gorjeta}")
print(f"Total a pagar: {total_com_gorjeta}")
print(f"Valor por pessoa: {valor_por_pessoa}")