import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import (QApplication, QLineEdit, QMainWindow, QPushButton,
                             QSpacerItem, QVBoxLayout, QLabel, QWidget,
                             QTableWidget, QTableWidgetItem, QComboBox)


class MainForm(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent=parent)

        # Nossa "Base de Dados" em memória
        self.FUNCIONATIOS = [
            {'nome': 'Osenias', 'sexo': 'Masculino'},
            {'nome': 'Izzie', 'sexo': 'Feminino'}
        ]

        # Componentes da Interface
        self.label_nome = QLabel('Nome do Colaborador:')
        self.edt_nome = QLineEdit()
        self.edt_nome.setPlaceholderText("Digite o nome completo...")

        self.label_sexo = QLabel('Sexo:')
        self.cb_sexo = QComboBox()
        self.cb_sexo.addItems(['Masculino', 'Feminino', 'Outro'])

        self.button_adicionar = QPushButton('Adicionar à Tabela')

        # CONEXÃO: Aqui ligamos o clique do botão à função que processa os dados
        self.button_adicionar.clicked.connect(self.clicando)

        # Configuração da Tabela
        self.table = QTableWidget()
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(['Nome', 'Sexo'])
        # Faz a tabela ocupar todo o espaço horizontal
        self.table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        # Layout
        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.label_nome)
        vertical_layout.addWidget(self.edt_nome)
        vertical_layout.addWidget(self.label_sexo)
        vertical_layout.addWidget(self.cb_sexo)
        vertical_layout.addWidget(self.button_adicionar)
        vertical_layout.addWidget(self.table)

        self.componentes = QWidget()
        self.componentes.setLayout(vertical_layout)
        self.setCentralWidget(self.componentes)

        self.setWindowTitle('Gestão de Equipa NAI-09')
        self.setGeometry(100, 100, 600, 500)

        # Popula a tabela com os dados iniciais
        self.popular_tabela()

    def popular_tabela(self):
        """Limpa e redesenha a tabela com os dados da lista self.FUNCIONATIOS"""
        self.table.setRowCount(len(self.FUNCIONATIOS))

        for linha, valor in enumerate(self.FUNCIONATIOS):
            item_nome = QTableWidgetItem(valor['nome'])
            item_sexo = QTableWidgetItem(valor['sexo'])

            # Centraliza o texto do sexo na célula
            item_sexo.setTextAlignment(QtCore.Qt.AlignCenter)

            self.table.setItem(linha, 0, item_nome)
            self.table.setItem(linha, 1, item_sexo)

    def clicando(self):
        """Método que processa o Input e atualiza o sistema"""
        # 1. Captura os dados dos inputs
        nome_digitado = self.edt_nome.text().strip()
        sexo_selecionado = self.cb_sexo.currentText()

        # 2. TRATAMENTO DE EXCEÇÃO: Validando se o nome não está vazio
        try:
            if not nome_digitado:
                # Levanta um erro se o campo estiver vazio
                raise ValueError("O campo nome é obrigatório!")

            # 3. Se estiver tudo OK, adiciona o novo dicionário à lista
            novo_registro = {
                'nome': nome_digitado,
                'sexo': sexo_selecionado
            }
            self.FUNCIONATIOS.append(novo_registro)

            # 4. ATUALIZAÇÃO: Chama a função para redesenhar a tabela com o novo dado
            self.popular_tabela()

            # 5. Limpeza: Limpa o campo de texto para o próximo cadastro
            self.edt_nome.clear()
            self.edt_nome.setFocus()
            print(f"Sucesso: {nome_digitado} adicionado à lista.")

        except ValueError as e:
            # Captura o erro e mostra no console (ou poderia ser um alerta na tela)
            print(f"ERRO DE VALIDAÇÃO: {e}")


# Execução
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainForm()
    main.show()
    sys.exit(app.exec_())