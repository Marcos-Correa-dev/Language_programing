def salvar_configuracao(nome_maquina, ip, temp_maxima):

    with open("config_maquina.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write(f"nome da maquina: {nome_maquina}\n")
        arquivo.write(f"Endereço Ip: {ip}\n")
        arquivo.write(f"Temperatura máxima: {temp_maxima}C\n")

    print(" Sucesso! o arquivo de configuração foi gravado.")

def ler_configuracao():
    with open("config_maquina.txt", "r", encoding="utf-8") as arquivo:
        conteudo = arquivo.read()
        print(conteudo)


# PROGRAMA PRINCIPAL - COMEÇA AQUI!

nome = input("Digiter o nome da máquina: ")
endereco_ip = input("Digite o IP da rede: ")
temperatura = float(input(" Digite a temperatura máxima: "))

salvar_configuracao(nome, endereco_ip, temperatura)
ler_configuracao()