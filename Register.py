from PyQt5 import QtWidgets, uic
import sys

class Register(QtWidgets.QMainWindow):
    def __init__(self):
        super(Register, self).__init__()
        uic.loadUi('Register.ui', self)

        self.button = self.findChild(QtWidgets.QPushButton, 'registerPageButton')
        self.button.clicked.connect(self.registerButtonPressed)
        self.input = self.findChild(QtWidgets.QLineEdit, 'id')
        self.input = self.findChild(QtWidgets.QLineEdit, 'password')
        self.show()

    def registerButtonPressed(self):
        # This is executed when the button is pressed
        print('ID:' + self.id.text())
        print('Password:' + self.password.text())

app = QtWidgets.QApplication(sys.argv)
window = Register()
app.exec_()