usuario = {"login": "operador_1", "permissoes": ["ler", "escrever"]}

usuario.update({"login": "supervisor_geral", "setor": "producao"})

usuario["permissoes"].append("deletar")

print(f"{usuario['login']} - {usuario['permissoes'][2]}")

