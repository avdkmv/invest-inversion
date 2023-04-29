import os
import talib
import numpy as np

ITERATION = int(os.getenv("ITERATION"))


def calculate_ema(candles):
    candlesNp = np.array(candles)
    return talib.EMA(candlesNp, ITERATION)[-1]
