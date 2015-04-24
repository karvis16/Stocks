import sys

# this file create some basic windows

from PySide.QtCore import *
from PySide.QtGui import *


def loginChallenge(yes = True):
    print "run login script"
    
def registerNewUser(yes = True):
    print "run Register script"
    
def browseFiles(yes = True):
    print "run browse file script"
    
def loadSavedFile(yes = True):
    print "run load script" 


# Location constants
UNFINALX = 10
UNFINALY = 60
PWFINALX = 10
PWFINALY  = 100
LOADFINALX = 20
LOADFINALY = 160


# normally we'd use QApplication(sys.argv), but apparently canopy already has a QApplication instance running and we can only create the one
qt_app = QApplication.instance()

widget = QWidget()
widget.setMinimumSize(400,200)
widget.setWindowTitle("Welcome to Stocks!")

# label creation
titleLabel = QLabel("<font color=red size=18>Welcome to Stocks!</font>", widget)
usernameLabel = QLabel("Username:", widget)
passwordLabel = QLabel("Password:", widget)
loadLabel = QLabel("Load a saved file: ", widget)

# button creation and placement
loginButton = QPushButton("Log in", widget)
loginButton.move( UNFINALX + 250, UNFINALY)
registerButton = QPushButton("Register new User", widget)
registerButton.move(PWFINALX + 250, PWFINALY)
browseButton = QPushButton("Browse", widget)
browseButton.move(LOADFINALX + 150, LOADFINALY-4)       # -4 is from the height offset between button dimension and label, to center on vertical centerline
loadButton = QPushButton("Load", widget)
loadButton.move(LOADFINALX+250, LOADFINALY-4)

# text input fields
usernameInput = QLineEdit(parent=widget)
usernameInput.setFixedWidth(150)
usernameInput.move(UNFINALX + 75, UNFINALY)
passwordInput = QLineEdit(parent= widget)
passwordInput.setFixedWidth(150)
passwordInput.move(PWFINALX + 75, PWFINALY)

# label logistics and placement
titleLabel.move(60,0)
usernameLabel.move(UNFINALX, UNFINALY)
passwordLabel.move(PWFINALX, PWFINALY)
loadLabel.move(LOADFINALX, LOADFINALY)

# set button behavior
loginButton.clicked.connect(loginChallenge)
registerButton.clicked.connect(registerNewUser)
browseButton.clicked.connect(browseFiles)
loadButton.clicked.connect(loadSavedFile)

# put on the screen
widget.show()
qt_app.exec_()
