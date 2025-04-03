from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication,QLCDNumber,QWidget,QDial,QMessageBox
import sys,sqlite3

class BancoEfeitos(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('carregarefeitos.ui', self)

        self.pushButton.clicked.connect(self.cerregaEfeito)
        self.pedalUI=TelaEfeitos()

    def cerregaEfeito(self):
        self.pedalUI.ui.show()


class TelaEfeitos(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi('pedalUI.ui', self)

        self.lcdCompressor=self.findChild(QLCDNumber,"lcdCompressor")#conecta com o lcd
        self.dial_compressor=self.findChild(QDial,"dial_compressor") #conecta com o botão
        self.dial_compressor.valueChanged.connect(self.alterar_dial_compressor)  #cria o sinal que conecta a função alterar dial
        

        self.volume.valueChanged.connect(self.alterar_slider) 
        self.valor_slider()
        
        self.pushButton.clicked.connect(self.botao_ligar)

        self.pushButton_2.clicked.connect(self.botao_desligar)

        self.pushButton_3.clicked.connect(self.salvar_efeito)

        self.lcdGanho=self.findChild(QLCDNumber,"lcdGanho") #falta
        self.dial_ganho=self.findChild(QDial,"dial_ganho") #falta
        self.dial.valueChanged.connect(self.alterar_dial_ganho) #conectando botao redondo (sinal)


        self.lcdPitch=self.findChild(QLCDNumber,"lcdPitch")#conecta com o lcd
        self.dial_pitch=self.findChild(QDial,"dial_pitch")
        self.dial_pitch.valueChanged.connect(self.alterar_dial_pitch) #conectando botao redondo (sinal)

        self.lcdDistorcao=self.findChild(QLCDNumber,"lcdDistorcao")#conecta com o lcd
        self.dial_distorcao=self.findChild(QDial,"dial_distorcao")
        self.dial_distorcao.valueChanged.connect(self.alterar_dial_distorcao) #conectando botao redondo (sinal)

        self.lcdRevebr=self.findChild(QLCDNumber,"lcdReverb")#conecta com o lcd
        self.dial_reverb=self.findChild(QDial,"dial_reverb")
        self.dial_reverb.valueChanged.connect(self.alterar_dial_reverb) #conectando botao redondo (sinal)

        self.lcdRazao=self.findChild(QLCDNumber,"lcdRazao")#conecta com o lcd
        self.dial_razao=self.findChild(QDial,"dial_razao")
        self.dial_razao.valueChanged.connect(self.alterar_dial_razao) #conectando botao redondo (sinal)

        self.lcdDelay=self.findChild(QLCDNumber,"lcdDelay")#conecta com o lcd
        self.dial_delay=self.findChild(QDial,"dial_delay")
        self.dial_delay.valueChanged.connect(self.alterar_dial_delay) #conectando botao redondo (sinal)

    def valor_slider(self):
        self.volume.setMinimum(0)
        self.volume.setMaximum(10)
        self.volume.setValue(1)
        

    def alterar_slider(self, valor):
        print(f'o volume esta em: {valor}')
        return valor


    def botao_ligar(self):
        print("a pedaleira está ligada")

    def botao_desligar(self):
        print("a pedaleira está desligada")


    def alterar_dial_ganho(self, valor): #redondo grande
        print(f'O ganho está em: {valor}')
        self.lcdGanho.display(valor)
        if valor < 5:
            self.lcdGanho.setStyleSheet("color: green;")
        elif 5 <= valor < 8:
            self.lcdGanho.setStyleSheet("color: yellow;")
        else:
            self.lcdGanho.setStyleSheet("color: red;")


    def alterar_dial_delay(self, valor): #redondo grande
        print(f'a saturação do delay está em: {valor}')
        self.lcdDelay.display(valor)
        if valor < 5:
            self.lcdDelay.setStyleSheet("color: green;")
        elif 5 <= valor < 8:
            self.lcdDelay.setStyleSheet("color: yellow;")
        else:
            self.lcdDelay.setStyleSheet("color: red;")


    def alterar_dial_pitch(self, valor): #redondo grande
        print(f'O pitch está em: {valor}')
        self.lcdPitch.display(valor)
        if valor < 5:
            self.lcdPitch.setStyleSheet("color: green;")
        elif 5 <= valor < 8:
            self.lcdPitch.setStyleSheet("color: yellow;")
        else:
            self.lcdPitch.setStyleSheet("color: red;")


    def alterar_dial_distorcao(self, valor): #redondo grande
        print(f'a saturação da distorcao está em: {valor}')
        self.lcdDistorcao.display(valor)
        if valor < 5:
            self.lcdDistorcao.setStyleSheet("color: green;")
        elif 5 <= valor < 8:
            self.lcdDistorcao.setStyleSheet("color: yellow;")
        else:
            self.lcdDistorcao.setStyleSheet("color: red;")


    def alterar_dial_compressor(self, valor): #redondo grande
        print(f'o compressor está em: {valor}')
        self.lcdCompressor.display(valor)
        if valor < 5:
            self.lcdCompressor.setStyleSheet("color: green;")
        elif 5 <= valor < 8:
            self.lcdCompressor.setStyleSheet("color: yellow;")
        else:
            self.lcdCompressor.setStyleSheet("color: red;")


    def alterar_dial_reverb(self, valor): #redondo grande
        print(f'a saturação do reverb está em: {valor}')
        self.lcdReverb.display(valor)
        if valor < 5:
            self.lcdReverb.setStyleSheet("color: green;")
        elif 5 <= valor < 8:
            self.lcdReverb.setStyleSheet("color: yellow;")
        else:
            self.lcdReverb.setStyleSheet("color: red;")

    
    def alterar_dial_razao(self, valor): #redondo grande
        print(f'a saturação da razao está em: {valor}')
        self.lcdRazao.display(valor)
        if valor < 5:
            self.lcdRazao.setStyleSheet("color: green;")
        elif 5 <= valor < 8:
            self.lcdRazao.setStyleSheet("color: yellow;")
        else:
            self.lcdRazao.setStyleSheet("color: red;")

    def salvar_efeito(self):
        compressor=self.dial_compressor.value()
        pitch=self.dial_pitch.value()
        volume=self.volume.value()
        reverb=self.dial_reverb.value()
        delay=self.dial_delay.value()
        distorcao=self.dial_distorcao.value()
        ganho=self.dial.value()
        razao=self.dial_razao.value()
        

        conexao=sqlite3.connect("efeitos.db")
        cursor=conexao.cursor()

        cursor.execute("""INSERT INTO SALVOS(compressor,pitch,volume,reverb,delay,distorcao,ganho,razao,volume) 
                       VALUES (?,?,?,?,?,?,?,?,?)""",(compressor,pitch,volume,reverb,delay,distorcao,ganho,razao,volume))

        conexao.commit()
        conexao.close()

        QMessageBox.information(self,"Efeito salvo","Efeito salvo com sucesso meo!")

    
    
    
class TelaInicial(QMainWindow):
    def __init__(self):  
        super().__init__()
        uic.loadUi('pedalinicio.ui', self)
        self.telaEfeitos=TelaEfeitos(parent=self)

        self.pushButton.clicked.connect(self.mostrar_tela)

        self.bancoEfeitos=BancoEfeitos()

        self.pushButton_2.clicked.connect(self.mostrar_banco)
    def mostrar_tela(self):
       
        self.telaEfeitos.show()    

    def mostrar_banco(self):
        self.bancoEfeitos.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    janela = TelaInicial()
    janela.show()
    sys.exit(app.exec_())
