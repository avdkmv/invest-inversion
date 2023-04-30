from tinkoff.invest import CandleInterval, Client
from tinkoff.invest.utils import now
from datetime import timedelta

from config import TINKOFF_TOKEN


def get_candles(figi):
    candles = []
    with Client(TINKOFF_TOKEN) as client:
        for candle in client.get_all_candles(
            figi=figi,
            from_=now() - timedelta(days=100),
            interval=CandleInterval.CANDLE_INTERVAL_30_MIN,
        ):
            candles.append(candle.close.units + candle.close.nano / 1000000000)
    return candles
