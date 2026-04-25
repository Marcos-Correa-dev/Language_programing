sistema = {
    "usuario": "dev_junior",
    "acessos": ["painel", "banco_de_dados"]
}
# Atualiza o usuário existente e cria a chave "status"
sistema.update({"usuario": "dev_senior", "status": "ativo"})

# Adicona um item no final da lista de acessos
sistema["acessos"].append("servidor_producao")

print(sistema["acessos"])