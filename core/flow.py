import logging
import time

from typing import List

from model import TickerData
from service import candles_service, ema_service, figi_service, macd_service

logger = logging.getLogger("invest-inversion")


def get_flow_info(tickers, iteration) -> List:
    if not tickers:
        raise ValueError(f"Trying to get flow info for empty tickers list")

    ticker_info = []

    for ticker_name in tickers:
        t = time.process_time()
        logger.info(f"Getting info for {ticker_name}")

        figi = figi_service.get_figi(ticker_name)
        candles = candles_service.get_candles(figi)[-iteration:]

        ema = round(ema_service.calc_ema(candles, iteration), 2)
        macd_fast, macd_slow, hist = macd_service.calc_macd(candles)

        macd_fast = round(macd_fast[-1], 2)
        macd_slow = round(macd_slow[-1], 2)
        hist = round(hist[-1], 2)

        ticker = TickerData(
            name=ticker_name,
            lastcandle=candles[iteration - 1],
            ema=ema,
            macdfast=macd_fast,
            macdslow=macd_slow,
            hist=hist,
        )
        ticker_info.append(ticker)
        logger.info(f"Got info for {ticker_name} in {time.process_time() - t}")

    return ticker_info
