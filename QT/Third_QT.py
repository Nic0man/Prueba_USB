#Primero ejecutar por consola el comando: pip install PyQt5
    #[notice] A new release of pip available: 22.3.1 -> 23.0.1
    #[notice] To update, run: python.exe -m pip install --upgrade pip

import sys
from PyQt5.QtWidgets import *

class MyGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initGUI()

    def initGUI(self):
        self.setGeometry(100,100,200,300)
        self.setWindowTitle('My simple GUI')

        #label = QLabel('Press the button below',self)
        label = QLabel(self)
        label.setText('Press the button below')
        label.move(10,30)

        self.textbox = QTextEdit(self)
        self.textbox.resize(180,100)
        self.textbox.move(10,60)

        #button = QPushButton('Press Me!',self)
        button = QPushButton(self)
        button.setText('Press Me!')
        button.resize(180,20)
        button.move(10,170)

        #button.clicked.connect(lambda: on_clicked(self.textbox.toPlainText()))
        button.clicked.connect(self.accion)
        self.show()

    def accion(self):
        msg = self.textbox.toPlainText()
        on_clicked(msg)


def main():
    app = QApplication([])
    window = MyGUI()
    sys.exit(app.exec_())

def on_clicked(msg):
    message = QMessageBox()
    message.setText(msg)
    message.exec_()


if __name__ == "__main__":
    main()