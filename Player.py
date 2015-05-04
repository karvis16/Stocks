"""
This file contains the player class, which houses individual player stats and
information. From their current stock, cash reserves, difficulty level, but 
also score history and various other entries that could be relevant
"""

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
        self.stocks.append((stockName, stockAmount))
        
    def calcScore(self):
        import pullDataRequestTest.PullCompanyinfo as PullStockInfo
        baseScore = -self.diffCash[self.difficulty]
        for i in self.stocks:
            stock = i[0]
            num = i[2]
            stockInfo = PullStockInfo(stock)
            baseScore+= num*stockInfo[1]
        return baseScore
        
    def loginChallenge(self, chalName, chalPW):
        # this is just for testing purposes, I plan to actually hash and properly implement a log in later
        return chalName==self.name and chalPW==self.passsword
        
    def getName(self):
        return self.name