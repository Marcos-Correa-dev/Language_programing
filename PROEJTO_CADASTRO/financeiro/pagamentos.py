
# financeiro/pagamentos.py

import config

def processar_pagamento(funcionario, imposto_calculado):
    # Vamos utilizar o GTTER.
    # O financeiro usa o Getter do RH para obter o salário

    salario_bruto =  funcionario.get_salario()
    salario_liquido = salario_bruto - imposto_calculado

    print("\n" + "="*30)
    print(f"HOLERITE DE PAGAMENTO")
    print("="*30)
    print(f"Funcionario: {funcionario.nome}")
    print(f"Cargo: {funcionario.cargo}")
    print(f"Salario Bruto: {config.MOEDA} {salario_bruto:.2f}")
    print(f"Desconto (imposto): {config.MOEDA} {imposto_calculado:.2f}")
    print("="*30)
    print(f"VALOR LÍQUIDO A RECEBER: {config.MOEDA} {salario_liquido:.2f}")
    print("="*30)