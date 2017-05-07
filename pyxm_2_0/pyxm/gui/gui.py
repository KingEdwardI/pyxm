#!/usr/bin/python3

import sys
from PyQt5.QtWidgets import (
        QMainWindow, 
        QApplication,
        QLabel,
        QLineEdit
        )

class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        # statusBar
        ready = True
        if ready:
            self.statusBar().showMessage('Ready')
        else:
            self.statusBar().showMessage('Not Ready')
        ##

        # lineEdit
        self.lbl = QLabel(self)
        qle = QLineEdit(self)
        qle.move(10,10)
        self.lbl.move(50,50)
        qle.textChanged[str].connect(self.onChangedText)

        ##
        
        self.setGeometry(400, 400, 350, 300)
        self.setWindowTitle('Statusbar')
        self.show()

    def onChangedText(self, text):

        self.lbl.setText(text)
        self.lbl.adjustSize()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

