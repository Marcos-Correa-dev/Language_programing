
# contabil/importos.py

#importando variáveis globais:

import config

def calcular_imposto_renda(salario_bruto):

    if salario_bruto > config.TETO_ISENCAO:
        imposto = salario_bruto * config.IMPOSTO_ALTO
    else:
        imposto = salario_bruto * config.IMPOSTO_BAIXO

    return imposto