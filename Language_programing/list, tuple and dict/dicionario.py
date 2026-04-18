# Definindo informações no dicionario

pessoa = {"nome": "Diogo", "idade": 32, "cidade": "Rj"}

for chave in pessoa:
    print("Chave: ", chave)
#
# print(pessoa["nome"])


#adicionando um dicionario vázio

# dicionario_vazio = dict()
# print(dicionario_vazio)

# Criando um dicionario com pares de chaves-de-valor

# dicionario_pessoa = dict(nome="Aline", idade=30, cidade="SP")
# print(dicionario_pessoa["nome"])


# Values -> retorna uma lista(ou view) dos valores do dicionario

# valores = pessoa.values()
# print(valores)

# Retorna uma lista (ou view) de pares chaves-de valores(tuplas)
# item = pessoa.items()
# print(item)

# utilizando o comando get
# estado = pessoa.get("estado")
# print(estado)


# Utilizando o comando update

# diferente = pessoa.update({"idade": 31, "cidade": "SP"})
# print(pessoa)


