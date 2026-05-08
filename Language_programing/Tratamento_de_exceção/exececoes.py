
# tratamento de exceções:

# try:
#     # É O CÓDIGO QUE PODE GERAR UMA EXCEÇÃO
#     resultado = 10 / 2
# except ZeroDivisionError:
#     # É o código que será execultado se  a exceção for capturada.
#     print("Erro: Não é possivel dividr por zero")
# else:
#     # Código que é execultado se nenhuma exceção for levantada.
#     print("Divisão realizada com sucesso")
# finally:
#     # Codigo que é sempre executado>
#     print("Finalizando Operação")




# try:
#     # É O CÓDIGO QUE PODE GERAR UMA EXCEÇÃO
#     arquivo = open("arquivo_inexistente.txt", "r")
#     resultado = 10 / 2
# except ZeroDivisionError:
#     # É o código que será execultado se  a exceção for capturada.
#     print("Erro: Não é possivel dividr por zero")
# except FileNotFoundError:
#     # Código que é execultado se nenhuma exceção for levantada.
#     print("ERRO: Arquivo não encontrado")
# except Exception as e:
#     # Codigo que é sempre executado>
#     print(f"Erro inesperado: {e}")



# def dividir(a,b):
#     if b == 0:
#         # serve para lançar exceções em execução especifica do programa
#         raise ValueError("O divisor não pode ser zero.")
#     return a / b
#
# try:
#     resultado = dividir(10,0)
# except ValueError as e:
#     print(f"Error: {e}")



