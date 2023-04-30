import talib
import numpy as np


def calc_ema(candles, iteration):
    candlesNp = np.array(candles)
    return talib.EMA(candlesNp, iteration)[-1]
