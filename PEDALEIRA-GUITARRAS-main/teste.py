from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QLCDNumber, QDial
import sys

class TelaEfeitos(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi('pedalUI.ui', self)

        # Encontra os widgets QDial e QLCDNumber pelo nome de objeto
        self.dial_compressor = self.findChild(QDial, "dial_compressor")
        self.lcdCompressor = self.findChild(QLCDNumber, "lcdCompressor")

        # Verifica se os widgets foram encontrados corretamente
        if self.dial_compressor is None:
            print("Erro: Não foi possível encontrar o QDial com o nome 'dial_compressor'.")
        if self.lcdCompressor is None:
            print("Erro: Não foi possível encontrar o QLCDNumber com o nome 'lcd_compressor'.")

        # Conecta o sinal valueChanged do QDial ao método alterar_dial_compressor
        if self.dial_compressor and self.lcdCompressor:
            self.dial_compressor.valueChanged.connect(self.alterar_dial_compressor)

    def alterar_dial_compressor(self, valor):
        print(f"O compressor está em: {valor}")
        self.lcdCompressor.display(valor)

        # Exemplo de mudança de cor do LCD com base no valor
        if valor < 50:
            self.lcdCompressor.setStyleSheet("color: green;")
        elif 50 <= valor < 80:
            self.lcdCompressor.setStyleSheet("color: yellow;")
        else:
            self.lcdCompressor.setStyleSheet("color: red;")

class TelaInicial(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('pedalinicio.ui', self)
        self.telaEfeitos = TelaEfeitos(parent=self)

        self.pushButton.clicked.connect(self.mostrar_tela)

    def mostrar_tela(self):
        self.telaEfeitos.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    janela = TelaInicial()
    janela.show()
    sys.exit(app.exec_())
