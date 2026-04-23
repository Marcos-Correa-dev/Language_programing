def calcular_conta_restaurante(*valores_pratos):
    # O python transforma os valores em uma tupla: (45.0, 30.0, 15.0)
    total = sum(valores_pratos)
    return total + (total * 0.10) # somando 10% do garçom

conta_mesa1 = calcular_conta_restaurante(45.0, 30.0, 15.0)
print(f"Mesa 1: R$ {conta_mesa1}")