import sys, os
from PyQt5 import QtCore, QtGui, QtWidgets
#  from PyQt5.QtWidgets import QApplication, QWidget
#  from PyQt5.QtGui import QIcon

#  class Example(QWidget):
    
    #  def __init__(self):
        #  super().__init__()

        #  self.initUI()

    #  def initUI(self):

        #  self.setGeometry(300,300,300,220)
        #  self.setWindowTitle('Simple')
        #  self.show()

if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    #  ex = Example()
    w = QtWidgets.QMainWindow()
    w.setWindowTitle('PyQt Demo')

    button = QtWidgets.QPushButton(w)
    button.setText('do thing')

    button.resize(100, 50)

    w.resize(250, 250)

    w.show()
    sys.exit(app.exec_())

