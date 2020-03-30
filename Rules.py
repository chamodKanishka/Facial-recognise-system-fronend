from PyQt5 import QtWidgets, uic
import sys

class Rules(QtWidgets.QMainWindow):
    def __init__(self):
        super(Rules, self).__init__()
        uic.loadUi('Rules.ui', self)


        self.show()



app = QtWidgets.QApplication(sys.argv)
window = Rules()
app.exec_()