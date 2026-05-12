# class AgenteSecreto:
#     def __init__(self, codinome, nome_real):
#         self.codinome = codinome     # todos podem acessar
#         self._nome_real = nome_real  # Privado: sofre Name Mangling
#
#
# agente = AgenteSecreto("007", "James Bond")
#
# # print(f"O espião chegou: {agente.codinome}")
#
# # Output:  O espião chegou: 007
#
# print(agente._nome_real)



# class SistemaGoverno:
#     def __init__(self):
#         self.__codigos_nucleares = "Alpha-Tango-99"
#
#
# brasil = SistemaGoverno()
#
# # print(brasil.__codigos_nucleares)
#
# print(brasil._SistemaGoverno__codigos_nucleares)



# class NaveEspacial:
#     def __init__(self, combustivel):
#         self.combustivel = combustivel
#
#     def __injetar_antimateria(self):
#         print("Injetando antimáteria no reator!")
#         self.combustivel -= 50
#
#     def iniciar_hiper_salto(self):
#         print("Preparando para o Hiper-salto...")
#         if self.combustivel >= 50:
#             self.__injetar_antimateria()
#             print("Salto concluído!")
#         else:
#             print("sem combustivel para o salto...")
#
# minha_nave = NaveEspacial(100)
#
#
#
# minha_nave.iniciar_hiper_salto()



