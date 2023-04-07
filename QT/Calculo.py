import sys
import PyQt5.QtWidgets as PyQt
from PyQt5.QtCore import Qt

class Calculo(PyQt.QWidget):
    def __init__(self):
        super().__init__()
        self.initGUI()
    
    def initGUI(self):
        self.setGeometry(300,300,220,170)
        self.setWindowTitle('First App')

        Titulo = PyQt.QLabel(self)
        Titulo.setText('Primera APP')
        Titulo.move(50,5)
        Titulo.setStyleSheet("QLabel{font-size: 18pt;}")

        self.num1 = PyQt.QLineEdit(self)
        self.num1.move(55,50)
        self.num1.resize(80,25)
        self.num1.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        self.num2 = PyQt.QLineEdit(self)
        self.num2.move(55,90)
        self.num2.resize(80,25)
        self.num2.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        num1txt = PyQt.QLabel(self)
        num1txt.setText('Número 1')
        num1txt.move(5,55)

        num2txt = PyQt.QLabel(self)
        num2txt.setText('Número2')
        num2txt.move(5,95)

        result = PyQt.QLabel(self)
        result.setText('Resultado')
        result.move(5,135)

        boton = PyQt.QPushButton(self)
        boton.setText('Calcular')
        boton.move(145,130)
        boton.resize(50,25)

        #Vlayout = PyQt.QVBoxLayout()

        self.b1 = PyQt.QRadioButton('Sumar',self)
        self.b1.setChecked(True)
        self.b1.move(145,45)
        #self.b1.clicked.connect(lambda: self.prueba(self.b1))
        #Vlayout.addWidget(self.b1)

        self.b2 = PyQt.QRadioButton('Restar',self)
        self.b2.move(145,65)
        #self.b2.clicked.connect(lambda: self.prueba(self.b2))
        #Vlayout.addWidget(self.b2)
        #self.setLayout(Vlayout)

        self.b3 = PyQt.QRadioButton('Multiplicar',self)
        self.b3.move(145,85)
        #self.b3.clicked.connect(lambda: self.prueba(self.b3))

        self.b4 = PyQt.QRadioButton('Dividir',self)
        self.b4.move(145,105)
        #self.b4.clicked.connect(lambda: self.prueba(self.b4))

        self.resultxt = PyQt.QLabel(self)
        self.resultxt.move(55,130)
        self.resultxt.resize(80,25)
        self.resultxt.setStyleSheet("QLabel{background-color: red;"\
        "font-weight: bold}")
        self.resultxt.setAlignment(Qt.AlignmentFlag.AlignCenter)

        boton.clicked.connect(self.calcular)

        # boton.clicked.connect(lambda: self.resultxt.setText(str(\
        #     int(self.num1.text())+int(self.num2.text()))))

        self.show()
        
    # def prueba(self,b):
    #     if b.isChecked() == True and b.text() == 'Sumar':
    #         print (f'{self.b1.text()} is selected')
    #     elif b.isChecked() == True and b.text() == 'Restar':
    #         print (f'{self.b2.text()} is selected')
    #     elif b.isChecked() == True and b.text() == 'Multiplicar':
    #         print (f'{self.b3.text()} is selected')
    #     else:
    #         print (f'{self.b4.text()} is selected')

    def calcular(self):
        if self.b1.isChecked() == True:
            self.resultxt.setText(str(\
                int(self.num1.text())+int(self.num2.text())))
        elif self.b2.isChecked() == True:
            self.resultxt.setText(str(\
                int(self.num1.text())-int(self.num2.text())))
        elif self.b3.isChecked() == True:
            self.resultxt.setText(str(\
                int(self.num1.text())*int(self.num2.text())))
        else:
            self.resultxt.setText(str(\
                int(self.num1.text())/int(self.num2.text())))           

def main():
    app = PyQt.QApplication([])
    inicio = Calculo()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()