import os
import talib
import numpy as np


def calculateMacd(candles):
    candlesNp = np.array(candles)
    return talib.MACD(candlesNp, 12, 26, 9)