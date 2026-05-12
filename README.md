markdown
# Repositório de Aulas Python: Arquitetura, POO e Tratamento de Exceções

Bem-vindo ao repositório de códigos e exemplos focados em consolidar os fundamentos avançados da linguagem Python. Este projeto marca a transição da programação estruturada básica para o desenvolvimento de software profissional, abordando **Orientação a Objetos (POO)**, **Sistemas Modulares** e **Segurança de Dados**.

---

##  Objetivos de Aprendizagem

Ao longo deste repositório, focamos em resolver problemas aplicando os seguintes pilares da engenharia de software:

* **Modularização:** Separação de responsabilidades (Clean Code). Divisão do sistema em arquivos de Regra de Negócio (Módulos/Classes) e arquivos de Interface (Programas Principais/Terminal).
* **Orientação a Objetos (POO):** Criação de Classes, Construtores (`__init__`) e Instanciação de Objetos.
* **Herança e Polimorfismo:** Reutilização de código através de superclasses e subclasses (`super()`), e reescrita de métodos genéricos para comportamentos específicos.
* **Encapsulamento (Proteção de Dados):** 
    * Atributos Públicos.
    * Atributos Protegidos (`_`).
    * Atributos Privados (`__`) utilizando o conceito de *Name Mangling* do Python.
* **Tratamento de Exceções:** Uso de `try`, `except`, `else` e `finally` para criar sistemas resilientes a falhas.
* **Levantamento de Erros (`raise`):** Criação de barreiras de segurança e regras de negócio disparando exceções personalizadas como `ValueError`.
* **Manipulação de Arquivos:** Leitura (`r`), Escrita (`w`), Adição (`a`) e manipulação de arquivos binários (`rb`, `wb`).

---

## Projetos e Cenários Desenvolvidos

A melhor forma de aprender arquitetura de software é na prática. Abaixo estão os principais miniprojetos presentes neste repositório:

### 1. Receive Hub (Automação Industrial)
* **Conceito:** Herança e Polimorfismo.
* **Descrição:** Sistema modular que simula o recebimento e organização de logs de fábrica. Diferencia pacotes de *Alarme* e pacotes de *Produção*, processando cada um de forma única.

### 2. BankHub (Segurança Bancária)
* **Conceito:** Encapsulamento Restrito e Lógica de Autenticação.
* **Descrição:** Simulação de uma conta bancária. Os atributos de `__saldo` e `__senha` são estritamente privados para garantir a segurança dos dados.

### 3. Projeto Bruxo (The Witcher)
* **Conceito:** Regras de Negócio com `raise` e Lógica de Encapsulamento.
* **Descrição:** Sistema para gerenciar a toxicidade do sangue de um bruxo. Se a poção consumida ultrapassar o limite tóxico seguro, o sistema bloqueia a ação disparando um erro fatal, evitando a overdose do personagem.

### 4. Laboratório de Exceções (Sci-Fi & Fantasia)
* **Conceito:** Fluxo de execução de Exceções (`try/except/else/finally`).
* **Descrição:** Scripts didáticos temáticos (Star Wars, Homem de Ferro, Senhor dos Anéis) que demonstram o caminho de execução do Python durante falhas de input e erros matemáticos (como `ZeroDivisionError`).

---

##  Estrutura Padrão dos Projetos

Os projetos modulares deste repositório seguem uma arquitetura de separação de arquivos para garantir a organização:
    
```
NOME_DO_PROJETO/
            ┣ modulo_classes.py 
# Contém apenas as Classes, Regras de Negócio e Encapsulamento. (Sem inputs de usuário) ┗ 
programa_principal.py 
# Importa as classes. Contém o loop de menu, inputs, prints e blocos try/except.
``` 

    

##  Como Clonar e Executar

Siga os passos abaixo para testar os códigos na sua máquina:

### 1. Pré-requisitos
* Ter o [Python 3.x](https://www.python.org/downloads/) instalado.
* Ter o [Git](https://git-scm.com/) instalado.

### 2. Clonando o Repositório
Abra o seu terminal (Prompt de Comando, PowerShell ou Terminal do Linux/Mac) e digite:
```


Clone o repositório para a sua máquina
git clone https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git
Entre na pasta do projeto recém-clonado
cd SEU_REPOSITORIO
``` 
*(Lembre-se de substituir o link acima pelo link real do seu repositório no GitHub)*

### 3. Executando os Códigos
Navegue até a pasta do projeto específico que deseja testar e execute o arquivo principal.
```
Exemplo executando a Jornada do Bruxo
cd Projeto_bruxo python jornada.py
``` 

> **Nota:** 
> Execute sempre o arquivo de interface (ex: `jornada.py`). Os módulos contendo as classes (ex: `mutacoes.py`) serão importados e utilizados automaticamente nos bastidores.

---

*"O código não precisa apenas funcionar, ele precisa ser seguro, modular e escalável."*
