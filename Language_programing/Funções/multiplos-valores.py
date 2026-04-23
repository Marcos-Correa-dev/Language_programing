# uma função que pode retornar multiplos valores usando uma tupla.

def dividir(a, b):
    quociente = a // b
    resto = a % b
    return quociente, resto

q, r = dividir(10, 3)
print(f"Quociente: {q}, Resto: {r}")