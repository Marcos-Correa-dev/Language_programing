# O sistema precisa registrar a entrada de uma mercadoria e
# gerar uma 'etiqueta visual' no console.
# Seu programa deve solicitar exatamente nesta ordem:
# O número do galpão (Inteiro).
# O código do produto (Inteiro).
# O peso da caixa (Float).
# O nome do conferente (String).
# Você deve imprimir um cabeçalho usando F-strings.
# Depois, você deve imprimir os dados da caixa
# (galpão, produto e peso)
# separados exatamente pelo símbolo | (use o parâmetro sep).
# Por fim, você deve gerar o 'Código de Rastreio',
# que é a junção do galpão, do produto e da sigla 'BR'
# totalmente colados, sem nenhum espaço (use o sep novamente)
print("-"*50)
num_galpao = int(input("digite"))
codigo_produto = int(input("digite"))
peso_faixa = float(input("digite"))
conferente = str(input("digite"))
print(f"nome : {conferente} ")
print(codigo_produto,peso_faixa,num_galpao, sep ="|")
print(f"codigo ratreio : {codigo_produto} {num_galpao} ","BR",sep ="")
