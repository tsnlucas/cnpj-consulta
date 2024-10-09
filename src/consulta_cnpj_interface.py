import sys
import requests
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QProgressBar, QTextEdit, QTabWidget, QLineEdit
from PyQt5.QtGui import QFont
from cnpj_consulta_thread import CNPJConsultaThread
from instrucoes_tab import InstrucoesTab

class CNPJConsultaApp(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Consulta de CNPJs')
        self.setGeometry(100, 100, 800, 600)

        title_font = QFont()
        title_font.setBold(True)
        title_font.setPointSize(16)

        self.layout = QVBoxLayout()

        self.tab_widget = QTabWidget(self)

        # Primeira aba: Consulta de CNPJs
        self.consulta_tab = QWidget()
        self.consulta_layout = QVBoxLayout()

        self.consultar_button = QPushButton('Iniciar Consulta')
        self.consultar_button.clicked.connect(self.consultar_cnpjs)
        self.consultar_button.setStyleSheet("background-color: #007acc; color: white")

        self.resultado_label = QLabel('Clique em "Iniciar Consulta" para começar.')
        self.resultado_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.resultado_label.setFont(title_font)

        self.progress_bar = QProgressBar(self)
        self.progress_bar.setValue(0)
        self.progress_bar.setMaximum(100)

        self.status_text = QTextEdit()
        self.status_text.setReadOnly(True)
        self.status_text.setStyleSheet("background-color: #f0f0f0; color: #333")

        self.cnpj_input = QLineEdit()
        self.cnpj_input.setPlaceholderText("Digite um CNPJ (apenas números, 14 dígitos)")
        self.cnpj_input.setMaxLength(14)

        self.consultar_cnpj_button = QPushButton("Consultar CNPJ")
        self.consultar_cnpj_button.clicked.connect(self.consultar_cnpj)

        self.limpar_log_button = QPushButton("Limpar Log")
        self.limpar_log_button.clicked.connect(self.limpar_log)

        self.consulta_layout.addWidget(self.resultado_label)
        self.consulta_layout.addWidget(self.consultar_button)
        self.consulta_layout.addWidget(self.progress_bar)
        self.consulta_layout.addWidget(self.status_text)
        self.consulta_layout.addWidget(self.cnpj_input)
        self.consulta_layout.addWidget(self.consultar_cnpj_button)
        self.consulta_layout.addWidget(self.limpar_log_button)

        self.consulta_tab.setLayout(self.consulta_layout)
        self.tab_widget.addTab(self.consulta_tab, 'Consulta de CNPJs')

        # Segunda aba: Instruções
        self.instrucoes_tab = InstrucoesTab()
        self.tab_widget.addTab(self.instrucoes_tab, 'Instruções')

        self.layout.addWidget(self.tab_widget)

        self.setLayout(self.layout)

        self.consulta_thread = None
        self.linhas_processadas = 0

    def consultar_cnpjs(self):
        self.resultado_label.setText('Consultando CNPJs, aguarde...')
        self.progress_bar.setValue(0)

        file_dialog = QFileDialog()
        arquivo_excel, _ = file_dialog.getOpenFileName(self, 'Selecione um arquivo Excel', '', 'Planilhas Excel (*.xlsx)')

        if arquivo_excel:
            self.limpar_log()  # Limpar o log antes de uma nova consulta
            self.consulta_thread = CNPJConsultaThread(arquivo_excel)
            self.consulta_thread.progress_signal.connect(self.atualizar_interface)
            self.consulta_thread.progress_percent_signal.connect(self.atualizar_progresso)
            self.consulta_thread.start()

    def consultar_cnpj(self):
        cnpj = self.cnpj_input.text()
        
        if not cnpj:
            self.status_text.append('O campo CNPJ está vazio.')
            return

        if not cnpj.isdigit() or len(cnpj) != 14:
            self.status_text.append('O CNPJ deve conter apenas números e ter exatamente 14 dígitos.')
            return

        self.limpar_log()  # Limpar o log antes de uma nova consulta
        self.status_text.append(f'Consultando CNPJ manualmente: {cnpj}')

        # URL para consultar o CNPJ no site
        url = f'https://www.receitaws.com.br/v1/cnpj/{cnpj}'

        try:
            response = requests.get(url)

            if response.status_code == 200:
                # Processar os dados da resposta JSON
                dados_receita = response.json()
                razao_social = dados_receita.get('nome', 'N/A')
                abertura = dados_receita.get('abertura', 'N/A')
                situacao = dados_receita.get('situacao', 'N/A')
                responsaveis = dados_receita.get('qsa', [{'nome': 'N/A'}])

                # Exibir os dados na caixa de texto
                self.status_text.append(f'Dados do CNPJ {cnpj}:')
                self.status_text.append(f'Razão Social: {razao_social}')
                self.status_text.append(f'Abertura: {abertura}')
                self.status_text.append(f'Situação: {situacao}')
                self.status_text.append('Responsáveis:')
                for responsavel in responsaveis:
                    self.status_text.append(f'- {responsavel["nome"]}')
            else:
                self.status_text.append('Erro na consulta. Verifique o CNPJ e tente novamente.')

        except Exception as e:
            self.status_text.append(f'Erro na consulta: {str(e)}')

    def limpar_log(self):
        self.status_text.clear()

    def atualizar_interface(self, mensagem):
        self.status_text.append(mensagem)

        if "Processo concluído" in mensagem:
            self.resultado_label.setText('Consulta Concluída')

    def atualizar_progresso(self, progresso):
        self.progress_bar.setValue(int(progresso))
        self.linhas_processadas = int(progresso) * self.linhas_processadas // 100

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CNPJConsultaApp()
    window.setStyleSheet("background-color: #f0f0f0")
    window.show()
    sys.exit(app.exec_())
