from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTextBrowser, QLabel
from PyQt5.QtGui import QPixmap

class InstrucoesTab(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.layout = QVBoxLayout()

        # Adicione o texto de instruções
        instrucoes_text = QTextBrowser()
        instrucoes_text.setPlainText("Instruções:\n\n1. Abra um arquivo Excel com a lista de CNPJs.\n2. Clique em 'Iniciar Consulta' para iniciar a consulta.\n3. Aguarde o término da consulta.\n4. Os resultados serão processados e salvos em um novo arquivo na mesma pasta onde o arquivo de dados foi importado, com '_editado' no nome.\n\nAbaixo, um exemplo de como o arquivo Excel deve ser estruturado:")

        # Carregue a imagem de exemplo e redimensione-a
        exemplo_image = QLabel()
        pixmap = QPixmap('imagens/exemplo.png')  # Caminho relativo para a imagem
        pixmap = pixmap.scaled(400, 400, Qt.KeepAspectRatio)  # Redimensione a imagem para 400x400 pixels
        exemplo_image.setPixmap(pixmap)

        self.layout.addWidget(instrucoes_text)
        self.layout.addWidget(exemplo_image)

        self.setLayout(self.layout)
