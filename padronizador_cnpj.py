import sys
import pandas as pd
import re
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog, QLabel, QMessageBox

def normalizar_cnpj(cnpj):
    """Remove qualquer formatação extra do CNPJ e garante que seja uma string com 14 dígitos."""
    cnpj = str(cnpj)
    cnpj = re.sub(r'\D', '', cnpj)  # Remove tudo que não for dígito
    return cnpj if len(cnpj) == 14 else None

def padronizar_excel_cnpjs(input_path, output_path):
    """Padroniza os CNPJs do arquivo Excel e salva um novo arquivo."""
    df = pd.read_excel(input_path)

    if 'CNPJ' not in df.columns:
        raise ValueError("Coluna 'CNPJ' não encontrada no arquivo.")

    df['CNPJ'] = df['CNPJ'].apply(normalizar_cnpj)
    df = df.dropna(subset=['CNPJ'])  # Remover linhas onde o CNPJ é inválido
    df.to_excel(output_path, index=False)

class CNPJPadronizadorApp(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Padronizador de CNPJs')
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()

        self.label = QLabel('Selecione um arquivo Excel para padronizar os CNPJs.')
        layout.addWidget(self.label)

        self.button_select = QPushButton('Selecionar Arquivo Excel')
        self.button_select.clicked.connect(self.select_file)
        layout.addWidget(self.button_select)

        self.button_padronizar = QPushButton('Padronizar e Salvar')
        self.button_padronizar.clicked.connect(self.padronizar)
        layout.addWidget(self.button_padronizar)

        self.setLayout(layout)
        self.input_path = None

    def select_file(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, 'Selecionar Arquivo Excel', '', 'Excel Files (*.xlsx)')
        if file_path:
            self.input_path = file_path
            self.label.setText(f'Arquivo selecionado: {file_path}')

    def padronizar(self):
        if not self.input_path:
            QMessageBox.warning(self, 'Erro', 'Por favor, selecione um arquivo primeiro.')
            return

        output_path = QFileDialog.getSaveFileName(self, 'Salvar Arquivo Padronizado', '', 'Excel Files (*.xlsx)')[0]
        if output_path:
            try:
                padronizar_excel_cnpjs(self.input_path, output_path)
                QMessageBox.information(self, 'Sucesso', f'Arquivo padronizado salvo em: {output_path}')
            except Exception as e:
                QMessageBox.critical(self, 'Erro', f'Erro ao padronizar o arquivo: {str(e)}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CNPJPadronizadorApp()
    window.show()
    sys.exit(app.exec_())
