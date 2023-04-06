#Primero ejecutar por consola el comando: pip install PyQt5
    #[notice] A new release of pip available: 22.3.1 -> 23.0.1
    #[notice] To update, run: python.exe -m pip install --upgrade pip
from PyQt5.QtWidgets import *

def main():
    app = QApplication([])
    window = QWidget()
    window.setGeometry(100,100,200,300)
    window.setWindowTitle('My simple GUI')

    layout = QVBoxLayout()

    label = QLabel('Press the button below')
    textbox = QTextEdit()
    button = QPushButton('Press Me!')

    button.clicked.connect(lambda: on_clicked(textbox.toPlainText()))

    layout.addWidget(label)
    layout.addWidget(textbox)
    layout.addWidget(button)

    window.setLayout(layout)

    window.show()
    app.exec_()

def on_clicked(msg):
    message = QMessageBox()
    message.setText(msg)
    message.exec_()


if __name__ == "__main__":
    main()
