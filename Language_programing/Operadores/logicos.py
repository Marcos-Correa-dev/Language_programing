# Definindo Valores
x = [1, 2, 3]
y = x # y e x referenciam o mesmo objeto
z = [1, 2, 3]  # "z" é um objeto diferente


# Comparação de identidade com o operador

resultado_is = x is y
print("resultado de x is y: ", resultado_is) # output: True


# Comparação de identidade com um objeto diferente
resultado_is_not = x is z
print("resultado de x is z: ", resultado_is_not)  #Output: False

# Usando 'is' com operadores lógicos

resulado_logico = x is y and z is not y
print("Resultado de x is y and is not y: ", resulado_logico) # True

