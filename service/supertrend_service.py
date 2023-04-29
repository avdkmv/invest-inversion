import numpy as np
import ta


def super_trend(close):
    # Inputs for calculation are the close prices of the financial instrument
    xtr = ta.trend()
    st = 10 * (xtr - close) + 10 * (close - xtr[::-1])
    std_st = ta.std(st)
    return np.where(st > close * (std_st * 2), 1, -1).cumsum(), std_st
