class Tarefa:
    # Método construtuor
    def __init__(self, descricao):
        self.descricao = descricao
        self.concluida = False

    # Método de Ação: Altera o estado do atributo
    def marcar_concluida(self):
        self.concluida = True
        print(f"Sucesso: A tareda {self.descricao} foi finalizada com sucesso!")


print(" --- Meu gerenciador de tarefas ---- ")

# Criando a tarefa (Instanciando)
minha_tarefa = Tarefa("Estudar para a prova de Python")

print(f"Tarefa: {minha_tarefa.descricao}")
print(f"Está concluída? {minha_tarefa.concluida}")  # Vai exibir False


# Executando a ação

print("\nTrabalhando na tarefa...")
minha_tarefa.marcar_concluida()

print(f"Status atual: {minha_tarefa.concluida}")  # Agora vai exibir True