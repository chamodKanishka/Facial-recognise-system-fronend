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
    w.setWindowTitle('Admin Page')
    label = QLabel(w)
    label.setText("Admin")
    label.setFont(QtGui.QFont("Arial", 20, QtGui.QFont.Bold))
    label.setStyleSheet("border-radius: 25px;border: 2px solid blue;")
    label.move(100,30)
    label.show()

    grid = QGridLayout(w)
    grid.setContentsMargins(50, 50, 50, 50)
    grid.addWidget(QLabel("Identification No"),0,0)
    grid.addWidget(QLineEdit(),0,1)
    grid.addWidget(QLabel("Password"),1,0)
    grid.addWidget(QLineEdit(),1,1)

    w.resize(300,300)
    w.show()
    sys.exit(app.exec_())
