import os
import talib
import numpy as np

ITERATION = int(os.getenv('ITERATION'))

class MacdService:

    def calculateMacd(candles):
        candlesNp = np.array(candles)
        return talib.MACD(candlesNp, 12, 26, 9)