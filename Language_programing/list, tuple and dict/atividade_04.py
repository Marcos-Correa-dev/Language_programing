# Atividade 2: O Carrinho de Compras Blindado (Tuplas + Dicionários + Funções de Lista) Nós temos o
# catálogo de uma loja de eletrônicos armazenado em um dicionário, e um cliente que já finalizou o pedido
# (os itens do pedido não podem mais ser alterados).
#
# Crie o dicionário catalogo: {"Mouse": 50.0, "Teclado": 120.0, "Monitor": 800.0, "Fone": 90.0} -  done
catalogo = {"Mouse": 50.0, "Teclado": 120.0, "Monitor": 800.0, "Fone": 90.0}
#
# Crie uma tupla chamada carrinho com os itens que o cliente comprou: ("Mouse", "Monitor", "Mouse")  - done

carrinho = ("Mouse", "Monitor", "Mouse")

# (Sim,ele comprou dois mouses!)
# Calcule o valor total da compra: Crie uma variável total = 0. - done
total = 0
# Faça um laço for que percorra a tupla carrinho. - done

for item in carrinho:
# Para cada item na tupla, busque o preço dele no dicionário catalogo e some à variável total. - done
    preco = catalogo[item]
    total += preco
# O Desafio do Estoque: O gerente quer saber exatamente quantos mouses foram vendidos nesse pedido.
# Use o método correto da tupla para contar quantas vezes a palavra "Mouse" aparece no carrinho e imprima
# o resultado. - done
qtd_resultados_mouses = carrinho.count("Mouse")
# Imprima o valor total da compra formatado.

print(f"Quantidade de Mouses vendidos: {qtd_resultados_mouses} .")
print(f"Valor total da compra: {total:.2f}")