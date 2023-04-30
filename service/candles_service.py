from typing import List

from tinkoff.invest import CandleInterval, Client
from tinkoff.invest.grpc.marketdata_pb2 import HistoricCandle
from tinkoff.invest.utils import now
from datetime import timedelta

from config import TINKOFF_TOKEN


def get_candles(figi) -> List[HistoricCandle]:
    candles = []
    with Client(TINKOFF_TOKEN) as client:
        for candle in client.get_all_candles(
                figi=figi,
                from_=now() - timedelta(days=100),
                interval=CandleInterval.CANDLE_INTERVAL_30_MIN,
        ):
            candles.append(candle)
    return candles


def get_close_price(candle):
    price = candle.close
    unit = price.units
    nano = price.nano
    return unit + (nano / 1000000000)


def get_high_price(candle):
    price = candle.high
    unit = price.units
    nano = price.nano
    return unit + (nano / 1000000000)


def get_low_price(candle):
    price = candle.low
    unit = price.units
    nano = price.nano
    return unit + (nano / 1000000000)
