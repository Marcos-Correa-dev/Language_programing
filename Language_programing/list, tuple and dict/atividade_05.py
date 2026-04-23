# O Sistema de Faltas (Foco no .get()) Você está criando um sistema para controlar as faltas
# dos alunos.
#
# Crie o dicionário faltas: {"Marcos": 2, "Ana": 0, "Carlos": 5} - done
faltas = {"Marcos": 2, "Ana": 0, "Carlos": 5}
# Peça ao usuário para digitar o nome de um aluno para consultar as faltas.
#
# Usando o método .get(), tente buscar o aluno digitado.
buscar_nome :str = str(input("digite um nome")).capitalize()
# Regra de ouro: Se o aluno não estiver no dicionário, o .get() deve retornar a string "Aluno não
# matriculado".
resultado = faltas.get(buscar_nome,"aluno nã cadastrado")
# Imprima o resultado na tela (ex: "Faltas do aluno X: 2" ou "Faltas do aluno Y: Aluno não matriculado").
print(resultado)