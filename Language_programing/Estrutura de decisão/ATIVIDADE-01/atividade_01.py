# temperatura = float(input("Qual a temperatura da caldeira? "))
#
# if temperatura < 50:
#     print("Operação normal")
# elif 50 <= temperatura <= 80: # Python aceita a sintaxe junto
#     print("Atenção: aquecimento moderado")
# elif 80 < temperatura < 100:
#     print("Alerta Laranja: Ativar ventilação")
# else:
#     print("Perigo: Evacuar seto!")


temperatura = float(input("Qual a temperatua da caldeira?"))

if temperatura < 50:
    print("Operação normal!")
else:
    if temperatura <= 80:
        print("Atenção: Aquecimento Moderado.")
    else:
        if temperatura < 100:
            print("Alerta laranja: Ativar ventilação")
        else:
            print("Perigo: Evacuar setor")