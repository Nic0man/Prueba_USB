import sys
import PyQt5.QtWidgets as PyQt
from PyQt5.QtCore import Qt

class Calculo(PyQt.QWidget):
    def __init__(self):
        super().__init__()
        self.initGUI()
    
    def initGUI(self):
        self.setGeometry(300,300,200,300)
        self.setWindowTitle('First App')

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
        boton.move(145,90)
        boton.resize(50,25)

        self.resultxt = PyQt.QLabel(self)
        self.resultxt.move(55,130)
        self.resultxt.resize(80,25)
        self.resultxt.setStyleSheet("QLabel {background-color: red;"\
        "font-weight: bold}")
        self.resultxt.setAlignment(Qt.AlignmentFlag.AlignCenter)

        boton.clicked.connect(self.suma)
        self.show()

    def suma(self):
        suma = int(self.num1.text())+int(self.num2.text())
        self.resultxt.setText(str(suma))
        

def main():
    app = PyQt.QApplication([])
    inicio = Calculo()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()