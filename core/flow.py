import os

from model import Ticker
from service import FigiService, CandlesService, EmaService, MacdService

TICKERS = os.getenv('TICKERS').split()
ITERATION = int(os.getenv('ITERATION'))

class Flow:

    def getInfo():
        tickers = []

        for tickerName in TICKERS:
            ticker = Ticker()
            ticker.setTicker(tickerName)

            figi = FigiService.getfigi(tickerName)
            candles = CandlesService.loadCandles(figi)
            ticker.setLastCandle(candles[ITERATION-1])

            ema = EmaService.calculateEma(candles)
            ticker.setEma(round(ema,2))
            
            macdFast, macdSlow, hist = MacdService.calculateMacd(candles)
            ticker.setMacdFast(round(macdFast[-1],2))
            ticker.setMacdSlow(round(macdSlow[-1],2))
            ticker.setHist(round(hist[-1],2))
            tickers.append(ticker)

        for ticker in tickers:
            print(ticker)
