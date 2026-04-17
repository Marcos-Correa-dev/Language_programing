#Exemplo combinando whiçe com break e continue

contador = 0
while contador < 10:
    contador += 2
    if contador == 7:
        continue # Pula a imprenssão do numero 5
    if contador == 8:
        break # Interrompe o laço ao alcançar o numero 8
    print(contador)