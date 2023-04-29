import os

from tinkoff.invest import CandleInterval, Client
from tinkoff.invest.utils import now
from datetime import timedelta

TOKEN = os.getenv("TOKEN")
ITERATION = int(os.getenv("ITERATION"))


def load_candles(figi):
    candles = []
    with Client(TOKEN) as client:
        for candle in client.get_all_candles(
            figi=figi,
            from_=now() - timedelta(days=100),
            interval=CandleInterval.CANDLE_INTERVAL_30_MIN,
        ):
            # print("candle = ", candle.close.units + candle.close.nano / 1000000000)
            candles.append(candle.close.units + candle.close.nano / 1000000000)
    return candles[-ITERATION:]
