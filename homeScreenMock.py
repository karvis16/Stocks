import sys

# this is a mock of the home screen of the game.

from PySide.QtCore import *
from PySide.QtGui import *

# define button behavior functions NB these need to be defined before they are called.
def analytics(yes = True):
    print "launch analytics screen"
    
def buyAction(yes = True):
    print "launch stock buy screen"
    
def sellAction(yes = True):
    print "launch stock sell screen"
    
def exitAction(yes = True):
    print "close application"
    
def loadSavedFile(yes = True):
    print "load a small screen to load a saved file"
    
def saveCurrentState(yes = True):
    print "return prompt on where to save the current state/name it"
    
def logoutAction(yes = True):
    print "return to log in screen"
    
def stockScreen(yes = True):
    print "launch the stock screen, with both buy and sell options"

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

#add some temp labels for now
label1 = QLabel("status",parent = statusOverviewWidget)
label2 = QLabel("stock info", parent = stockOverviewWidget)
label3 = QLabel("options:", parent = optionsWidget)

# create the list of stocks that are owned


# populate the options widget and place buttons
viewStocksButton = QPushButton("View Stocks", parent = optionsWidget)
viewStocksButton.move(BUTTONLOFFSETX, 1*BUTTONOFFSETY)
viewStocksButton.setFixedWidth(244)
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
analyticsButton.setFixedWidth(244)
exitButton = QPushButton("Exit", parent = optionsWidget)
exitButton.move(BUTTONLOFFSETX,6*BUTTONOFFSETY)
logoutButton = QPushButton("Log out", parent = optionsWidget)
logoutButton.move(BUTTONROFFSETX,6*BUTTONOFFSETY)

# set button behavior
analyticsButton.clicked.connect(analytics)
buyButton.clicked.connect(buyAction)
exitButton.clicked.connect(exitAction)
loadButton.clicked.connect(loadSavedFile)
saveButton.clicked.connect(saveCurrentState)
logoutButton.clicked.connect(logoutAction)
sellButton.clicked.connect(sellAction)
viewStocksButton.clicked.connect(stockScreen)

# put on the screen
mainWidget.show()
qt_app.exec_()