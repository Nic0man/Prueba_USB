from PyQt5.QtWidgets import *
from PyQt5 import uic

class myGUI(QMainWindow):
    def __init__(self):
        super(myGUI, self).__init__()
        uic.loadUi('myGUI.ui', self)
        self.show()

        self.pushButton.clicked.connect(self.login)
        self.pushButton_2.clicked.connect(lambda: self.sayit(self.textEdit.toPlainText()))
        self.actionClose.triggered.connect(exit)

    def login(self):
        if self.lineEdit.text() == "david" and self.lineEdit_2.text() == 'contraseña':
            self.textEdit.setEnabled(True)
            self.pushButton_2.setEnabled(True)
        else:
            message = QMessageBox()
            message.setText('Login invalido')
            message.exec_()

    def sayit(self,msg):
        message = QMessageBox()
        message.setText(msg)
        message.exec_()

def main():
     app = QApplication([])
     window = myGUI()
     app.exec_()


if __name__ == "__main__":
    main()
