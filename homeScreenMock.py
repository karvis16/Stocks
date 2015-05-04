import sys

# this is a mock of the home screen of the game.

from PySide.QtCore import *
from PySide.QtGui import *
from pullDataRequestTest import PullCompanyInfo, PullCompanyHistory, CleanPulledInfo, PlotInfo
#from embedding_in_qt4 import MyMplCanvas, MyStaticMplCanvas, ApplicationWindow


class Player:
    
    diffCash = {'easy' : 1000000, 'medium' : 100000, 'hard' : 10000}
    stocks = []
    
    def __init__(self, name, password, difficulty):
        # prompt player to create 
        self.name = name
        self.passwor = password
        self.difficulty = difficulty
        self.cash = self.diffCash[difficulty]
        
    def getDifficulty(self):
        return self.difficulty
        
    def addStock(self, stockName, stockAmount):
        cost = stockAmount* self.stockWorth(stockName)
        if cost <= self.cash:
            self.stocks.append((stockName, stockAmount))
            self.reduceCash(cost)
        else:
            pass
        
    def removeStock(self, stockName, stockAmount):
        # return nothing, but update the cash value with the stock sold's value
        for i in self.stocks:
            if stockName == i[0]:
                if i[1] >= stockAmount:
                # default is to just sell all if we ask to remove more than we have
                    amount = i[1]
                    self.stocks.remove(i)
                else:
                    amount = stockAmount
                    i[1] = i[1]-amount
                cash = self.stockWorth(i[0])
                self.addCash(cash)
                
                
        
    def stockWorth(self, stock):
        from pullDataRequestTest import PullCompanyInfo as PullStockInfo
        stockInfo = PullStockInfo(stock)
        return stockInfo[1]
        
    def setCash(self, amount):
        self.cash = amount
    
    def getCash(self):
        return self.cash
        
    def reduceCash(self, amount):
        self.cash-= amount
    
    def addCash(self, amount):
        self.cash += amount
        
    def calcScore(self):
        from pullDataRequestTest import PullCompanyInfo as PullStockInfo
        baseScore = -self.diffCash[self.difficulty]
        for i in self.stocks:
            stock = i[0]
            num = i[1]
            stockInfo = PullStockInfo(stock)
            baseScore+= num*stockInfo[1]
        return baseScore + self.getCash()
        
    def loginChallenge(self, chalName, chalPW):
        # this is just for testing purposes, I plan to actually hash and properly implement a log in later
        return chalName==self.name and chalPW==self.passsword
        
    def getName(self):
        return self.name

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

# attempting to fill the background of the status widget
p = statusOverviewWidget.palette()
p.setColor(statusOverviewWidget.backgroundRole(), Qt.red)
statusOverviewWidget.setPalette(p)

#add some temp labels for now
label1 = QLabel("status",parent = statusOverviewWidget)
label2 = QLabel("stock info", parent = stockOverviewWidget)
label3 = QLabel("options:", parent = optionsWidget)


# test player account
# create the list of stocks that are owned
# test stocks now with: 500 of google, disney and microsoft and $5000 cash
stocksOwned = [("GOOG", 500), ("DIS", 500), ("MSFT", 500)]
cashOwned = 5000
defaultPlayer = Player("Bob", "pepperoni", "hard")
defaultPlayer.setCash(100000000000)
for i in stocksOwned:
    print "adding {} stocks of {}".format(i[1], i[0])
    defaultPlayer.addStock(i[0], i[1])
defaultPlayer.setCash(cashOwned)
score = defaultPlayer.calcScore()

# create the personalized welcome screen and display the score
welcomeText = "Welcome {}".format(defaultPlayer.getName())
welcomeLabel = QLabel("<font size=18>"+welcomeText+"</font>", parent=statusOverviewWidget)
welcomeLabel.move(100,10)
welcomeLabel.setFont('Courier')
welcomeLabel.show()
scoreText = QLabel("Your current score is: {}".format(score), parent=statusOverviewWidget)
scoreText.move(10, 100) 




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