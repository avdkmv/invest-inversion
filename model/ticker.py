
class Ticker:

    def setTicker(self, ticker):
        self.ticker = ticker
    
    def setLastCandle(self, candle):
        self.candle = candle

    def setEma(self, ema):
        self.ema = ema

    def setMacdFast(self, macdFast):
        self.macdFast = macdFast

    def setMacdSlow(self, macdSlow):
        self.macdSlow = macdSlow

    def setHist(self, hist):
        self.hist = hist

    def __str__(self):
        return("Ticker = "+str(self.ticker)+" Last close price = "+str(self.candle)+
               " EMA = "+str(self.ema)+" macdFast = "+str(self.macdFast)+
               " macdSlow = "+str(self.macdSlow)+" hist = "+str(self.hist))