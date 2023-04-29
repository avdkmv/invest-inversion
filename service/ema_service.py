import os
import talib
import numpy as np

ITERATION = int(os.getenv('ITERATION'))

class EmaService:
    def calculateEma(candles):
        candlesNp = np.array(candles)
        return talib.EMA(candlesNp,ITERATION)[-1]