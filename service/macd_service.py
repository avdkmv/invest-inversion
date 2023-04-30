import talib
import numpy as np


def calc_macd(candles):
    candlesNp = np.array(candles)
    return talib.MACD(candlesNp, 12, 26, 9)
