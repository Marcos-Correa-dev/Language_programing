# O Carrinho de Compras Complexo (Foco no .update() e .append()) Imagine que um
# usuário está comprando online e adiciona itens ao carrinho, mas nós queremos organizar isso dentro de
# um dicionário chamado pedido.
#
# Crie o dicionário inicial: pedido = {"cliente": "Léo", "itens": ["Notebook"]} done
#
# O usuário escolheu mais dois itens. Usando o método .append(), adicione a String "Mouse" e a String
# "Teclado" à lista que está dentro da chave "itens" do dicionário pedido. done
#
# O usuário decidiu atualizar os dados de entrega. Usando o método .update(), adicione duas novas chaves
# ao dicionário pedido: "frete" com valor 25.50 e "status" com valor "Em Processamento".done
#
# Ao final, use um laço for com .items() para imprimir todas as chaves e valores do dicionário pedido
# atualizado.

pedido = {"cliente": "Léo", "itens": ["Notebook"]}
pedido["itens"].append("mouse")
pedido["itens"].append("teclado")

pedido.update({"frete": 25.50, "status":"Em Processamento"})
for chave,valor in pedido.items():
    print(f"{chave}: {valor}")




