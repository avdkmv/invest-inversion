import os
import talib
import numpy as np

ITERATION = int(os.getenv('ITERATION'))


def calculateEma(candles):
    candlesNp = np.array(candles)
    return talib.EMA(candlesNp,ITERATION)[-1]