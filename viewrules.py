import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPalette
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QMessageBox, QLineEdit, QRadioButton
        
if __name__ == "__main__":
    app = QApplication([])
 
    

    qp = QPalette()
    qp.setColor(QPalette.ButtonText, Qt.black)
    qp.setColor(QPalette.Window, Qt.gray)
    qp.setColor(QPalette.Button, Qt.blue)
    app.setPalette(qp)

    w = QWidget()
    w.setWindowTitle('View Rules')
    label = QLabel(w)
    label.setText("Our Rules")
    label.setFont(QtGui.QFont("Arial", 26, QtGui.QFont.Bold))
    label.setStyleSheet("border-radius: 25px;border: 2px solid blue;")
    label.move(230,30)
    label.show()


    w.resize(600,600)
    w.show()
    sys.exit(app.exec_())
