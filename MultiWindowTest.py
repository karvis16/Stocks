# test to see if I can have an underlying script run and control which widget/screen is visible

import sys

from PySide.QtCore import *
from PySide.QtGui import *

window = 1

def button1Press(self, t = True):
    window[1].show()
    window[0].hide()

def button2Press(self, t = True):
    window[0].show()
    window[1].hide()

app = QApplication.instance()
mainWidget = QWidget()
mainWidget.setWindowTitle("mainWidget")

class Window1(QMainWindow):
    def __init__(self):
        print "init window1"
        QMainWindow.__init__(self)
        widget1 = QWidget()
        widget1.setMinimumSize(400,300)
        widget1.setWindowTitle("window1")

        button1 = QPushButton("button1", widget1)
        button1.move(100,100)
        button1.clicked.connect(button1Press)


        widget1.show()
    
class Window2(QWidget):
    def __init__(self):
        print "init window 2"
        widget2 = QWidget()
        widget2.setMinimumSize(500,400)
        widget2.setWindowTitle("window2")
    
        button2 = QPushButton("button2", widget2)
        button2.move(0,0)
        button2.clicked.connect(button2Press)
        
        widget2.show()
    
if __name__ == '__main__':
    window = []
    w1 = Window1()
    w2 = Window2()
    window.append(w1)
    window.append(w2)
    window[0].show()
    app.exec_()