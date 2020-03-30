from PyQt5 import QtWidgets, uic
import sys

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('Home.ui', self)

        self.show()
        self.button1 = self.findChild(QtWidgets.QPushButton, 'registerButton')
        self.button1.clicked.connect(self.registerButtonPressed)
        self.button2 = self.findChild(QtWidgets.QPushButton, 'markButton')
        self.button2.clicked.connect(self.markButtonPressed)
        self.button3 = self.findChild(QtWidgets.QPushButton, 'downloadButton')
        self.button3.clicked.connect(self.downloadButtonPressed)
        self.button4 = self.findChild(QtWidgets.QPushButton, 'rulesButton')
        self.button4.clicked.connect(self.rulesButtonPressed)

    
    
    def registerButtonPressed(self):
        # This is executed when the button is pressed
        print('Register Button Clicked')

    def markButtonPressed(self):
        # This is executed when the button is pressed
        print('Mark Button Clicked')

    def downloadButtonPressed(self):
        # This is executed when the button is pressed
        print('Download Report Button Clicked')

    def rulesButtonPressed(self):
        # This is executed when the button is pressed
        print('View Rules Button Clicked')




app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()