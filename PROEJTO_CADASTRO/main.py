# fazendo as importações necessárias:
import config
from rh.models import Funcionario
from contabil.impostos import calcular_imposto_renda
from financeiro.pagamentos import processar_pagamento

def iniciar_sistema():
    print(f"-------- BE-VINDO AO ERP DA {config.NOME_EMPRESA} ----")

    # PASSO 1: RH: RECURSOS HUMANOS --
    print("\n[1] MÓDULO RH: Nova Contratação")
    nome_input = input("Digite o nome: ")
    cpf_input = input("Digite o CPF: ")
    cargo_input = input("Digite o cargo: ")
    salario_input = float(input("Dogote o salário bruto (exemplo> 3500.50): "))

    # PASSO 2: criando o objeto(variável) com os dados digitados
    novo_colaborador = Funcionario(nome_input,
                         cpf_input,
                         cargo_input, salario_input)

    print(f"--- SUCESSO! Colaborador registrado no RH.")

    # PASSO 3: Pausa para o utilizado acompanhar

    input("\nPressione ENTER para enviar os dados para a Contabilidade...")


    # PASSO 4: CONTABILIDADE
    print("\n[2] MÓDULO CONTÁBIL: Cálculo de Tributos")
    # lendo meu salário encapsulado
    salario_base = novo_colaborador.get_salario()
    #passar para função contabil
    imposto_retido = calcular_imposto_renda(salario_base)
    print(f"---- Imposto calculado com sucesso!: R$ {imposto_retido:.2f}")

    input("\nPressione ENTER para enviar a folha para o Financeiro...")


    # Passo 5: Financeiro
    print("\n[3] Módulo FINANCEIRO: Fechamento de Folha")

    # passando o objeto inteiro e o imposto calculado
    processar_pagamento(novo_colaborador, imposto_retido)
    input("\n=== OPERAÇÃO FINALIZADA ===")

if __name__ == "__main__":
    iniciar_sistema()
