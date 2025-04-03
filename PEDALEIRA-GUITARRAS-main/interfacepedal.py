
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('pedalUI.ui', self)


        self.pushButton_3.clicked.connect(self.botao_salvar)

        self.volume.valueChanged.connect(self.alterar_slider) 
        self.valor_slider()

        self.pushButton.clicked.connect(self.botao_ligar)

        self.pushButton_2.clicked.connect(self.botao_desligar)

        self.dial.valueChanged.connect(self.alterar_dial_ganho) #conectando botao redondo (sinal)
        self.valor_dial_ganho()


        self.dial_pitch.valueChanged.connect(self.alterar_dial_pitch) #conectando botao redondo (sinal)
        self.valor_dial_pitch()

        self.dial_distorcao.valueChanged.connect(self.alterar_dial_distorcao) #conectando botao redondo (sinal)
        self.valor_dial_distorcao()

        self.dial_compressor.valueChanged.connect(self.alterar_dial_compressor) #conectando botao redondo (sinal)
        self.valor_dial_compressor()

        self.dial_reverb.valueChanged.connect(self.alterar_dial_reverb) #conectando botao redondo (sinal)
        self.valor_dial_reverb()

        self.dial_razao.valueChanged.connect(self.alterar_dial_razao) #conectando botao redondo (sinal)
        self.valor_dial_razao()

        self.dial_delay.valueChanged.connect(self.alterar_dial_delay) #conectando botao redondo (sinal)
        self.valor_dial_delay()
    
    def valor_slider(self):
        self.volume.setMinimum(0)
        self.volume.setMaximum(10)
        self.volume.setValue(1)
        

    def alterar_slider(self, valor):
        print(f'o volume esta em: {valor}')


    def botao_salvar(self):
        print("os efeitos foram salvos!")


    def botao_ligar(self):
        print("a pedaleira está ligada")

    def botao_desligar(self):
        print("a pedaleira está desligada")

    def valor_dial_ganho(self): #colocar valores no botao redondo grande
        self.dial.setMinimum(0)
        self.dial.setMaximum(10)
        self.dial.setValue(1)

    def alterar_dial_ganho(self, valor): #redondo grande
        print(f'O ganho está em: {valor}')


    def valor_dial_delay(self): #colocar valores no botao redondo grande
        self.dial.setMinimum(0)
        self.dial.setMaximum(10)
        self.dial.setValue(1)

    def alterar_dial_delay(self, valor): #redondo grande
        print(f'a saturação do delay está em: {valor}')

    def valor_dial_pitch(self): #colocar valores no botao redondo grande
        self.dial.setMinimum(0)
        self.dial.setMaximum(10)
        self.dial.setValue(1)

    def alterar_dial_pitch(self, valor): #redondo grande
        print(f'O pitch está em: {valor}')

    def valor_dial_distorcao(self): #colocar valores no botao redondo grande
        self.dial.setMinimum(0)
        self.dial.setMaximum(10)
        self.dial.setValue(1)

    def alterar_dial_distorcao(self, valor): #redondo grande
        print(f'a saturação da distorcao está em: {valor}')

    def valor_dial_compressor(self): #colocar valores no botao redondo grande
        self.dial.setMinimum(0)
        self.dial.setMaximum(10)
        self.dial.setValue(1)

    def alterar_dial_compressor(self, valor): #redondo grande
        print(f'o compressor está em: {valor}')

    def valor_dial_reverb(self): #colocar valores no botao redondo grande
        self.dial.setMinimum(0)
        self.dial.setMaximum(10)
        self.dial.setValue(1)

    def alterar_dial_reverb(self, valor): #redondo grande
        print(f'a saturação do reverb está em: {valor}')

    def valor_dial_razao(self): #colocar valores no botao redondo grande
        self.dial.setMinimum(0)
        self.dial.setMaximum(10)
        self.dial.setValue(1)

    def alterar_dial_razao(self, valor): #redondo grande
        print(f'a saturação da razao está em: {valor}')


    def valor_dial_delay(self): 
        self.dial.setMinimum(0)
        self.dial.setMaximum(10)
        self.dial.setValue(1)

    def alterar_dial_delay(self, valor): 
        print(f'a saturação do delay está em: {valor}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    janela = MainWindow()
    janela.show()
    sys.exit(app.exec_())

