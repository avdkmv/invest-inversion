import os

ITERATION = int(os.getenv('ITERATION'))


def get_ema(candle, ema):
    price = candle
    alpha = 2 / (ITERATION + 1)
    return (alpha * price) + (1 - alpha) * ema


def calc_simple_ema(candles):
    innerCandles = candles
    prevEma = innerCandles.pop(0)
    for candle in innerCandles:
        prevEma = get_ema(candle, prevEma)
    return prevEma
