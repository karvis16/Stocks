import sys

# this is a mock of the home screen of the game.

from PySide.QtCore import *
from PySide.QtGui import *

qt_app = QApplication.instance()
mainWidget = QWidget()
mainWidget.setMinimumSize(800,600)
mainWidget.setWindowTitle("Stocks!")

#use this file to test widget within widgets

#constants
WIDGETSPLITX = 400 
WIDGETSPLITY = 200
BUTTONLOFFSETX = 50
BUTTONROFFSETX = 200
BUTTONOFFSETY = 50

# use 3 different widgets
statusOverviewWidget = QWidget(mainWidget)
statusOverviewWidget.move(0,0)
stockOverviewWidget = QWidget(mainWidget)
stockOverviewWidget.move(0,WIDGETSPLITY)
optionsWidget = QWidget(mainWidget)
optionsWidget.move(WIDGETSPLITX,WIDGETSPLITY)

#add some labels for now
label1 = QLabel("status",parent = statusOverviewWidget)
label2 = QLabel("stock info", parent = stockOverviewWidget)
label3 = QLabel("options:", parent = optionsWidget)


# populate the options widget and place buttons
viewStocksButton = QPushButton("View Stocks", parent = optionsWidget)
viewStocksButton.move(BUTTONLOFFSETX, 1*BUTTONOFFSETY)
saveButton = QPushButton("Save", parent = optionsWidget)
saveButton.move(BUTTONLOFFSETX,2*BUTTONOFFSETY)
loadButton = QPushButton("Load", parent = optionsWidget)
loadButton.move(BUTTONROFFSETX,2*BUTTONOFFSETY)
buyButton = QPushButton("Buy", parent = optionsWidget)
buyButton.move(BUTTONLOFFSETX,3*BUTTONOFFSETY)
sellButton = QPushButton("Sell", parent = optionsWidget)
sellButton.move(BUTTONROFFSETX,3*BUTTONOFFSETY)
analyticsButton = QPushButton("Analytics", parent = optionsWidget)
analyticsButton.move(BUTTONLOFFSETX,4*BUTTONOFFSETY)
exitButton = QPushButton("Exit", parent = optionsWidget)
exitButton.move(BUTTONLOFFSETX,6*BUTTONOFFSETY)
logoutButton = QPushButton("Log out", parent = optionsWidget)
logoutButton.move(BUTTONROFFSETX,6*BUTTONOFFSETY)


# put on the screen
mainWidget.show()
qt_app.exec_()