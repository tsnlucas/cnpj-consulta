import sys
from PyQt5.QtWidgets import QApplication
from cnpj_consulta_app import CNPJConsultaApp

def main():
    app = QApplication(sys.argv)
    window = CNPJConsultaApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
