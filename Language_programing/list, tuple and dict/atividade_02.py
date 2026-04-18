registro_aulas = ("java", "nodejs", "Oracle", "Python", "SQL")

print("-Analisando os registro de aula -")

quantidade_de_ocorrencia = registro_aulas.count("Python")
print(f"A disciplina 'Python' aparece {quantidade_de_ocorrencia} vezes no registro.")



posicao_sql = registro_aulas.index("SQL")
print(f"A disciplina 'SQL' aparece pela primeira vez no índice: {posicao_sql}.")