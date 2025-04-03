from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('pedalinicio.ui', self)

        #self.pushButton.clicked.connect(self.botao_pedaleira)

        #self.pushButton_2.clicked.connect(self.botao_efeitos)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    janela = MainWindow()
    janela.show()
    sys.exit(app.exec_())