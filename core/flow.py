import os
import logging

from typing import List

from model import TickerData
from service import candles_service, ema_service, figi_service, macd_service

try:
    TICKERS = os.environ['TICKERS'].split()
    ITERATION = int(os.environ['ITERATION'])
except Exception as e:
    print("No env")

FORMAT = '%(asctime)s %(clientip)-15s %(user)-8s %(message)s'

def get_flow_info() -> List:
    tickers = []

    for ticker_name in TICKERS:
        print(f"Getting info for {ticker_name}")

        figi = figi_service.getfigi(ticker_name)
        candles = candles_service.loadCandles(figi)
        ema = round(ema_service.calculateEma(candles), 2)
        macd_fast, macd_slow, hist = macd_service.calculateMacd(candles)

        macd_fast = round(macd_fast[-1],2)
        macd_slow = round(macd_slow[-1],2)
        hist = round(hist[-1],2)

        ticker = TickerData(name=ticker_name, lastcandle=candles[ITERATION-1], ema=ema, macdfast=macd_fast, macdslow=macd_slow, hist=hist)
        tickers.append(ticker)


    return tickers
