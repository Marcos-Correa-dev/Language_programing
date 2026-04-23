# O Python permite a utilização de parâmetros dinâmicos.

# *args permite que você passe um número variável de argumentos
# posicionais para uma função,

# def soma(*args):
#     resultado = 0
#     for num in args:
#         resultado += num
#     return resultado
#
# print(soma(1,2,3,4))  #Output: 10
# print(soma(10,20))  #Output: 30



# def verificar_acesso(cracha):
#     if cracha == "admin123":
#         print("Acesso liberado à sala de servidores!")
#     else:
#         print("Acesso negado, intruso detectado!")
#
# # verificar_acesso("visitante")
# verificar_acesso("admin123")


# def gerar_email_corporativo(nome, sobrenome):
#     email = f"{nome}.{sobrenome}@honda.com.br"
#     return  email
#
# novo_email = gerar_email_corporativo(input("Digite o nome: "),
#                                      input("digite o sobrenome"))
# print(f"Enviando mensagem de boas-vindas para: {novo_email}")

def cadastrar_usuario(nome, idade, cidade="Manaus"):
    status = "Maior de idade" if idade >= 18 else "Menor de idade"
    # retornando duas informações de uma vez só
    return nome, status, cidade

# Passando todos os dados
usuario1 = cadastrar_usuario("Alice", 26, "Sao Paulo")
usuario2 = cadastrar_usuario("Carlos", 16)

print(usuario1) #
print(usuario2)