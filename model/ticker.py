import dataclasses


@dataclasses.dataclass
class TickerData:
    name: str
    lastcandle: int
    ema: int
    macdfast: int
    macdslow: int
    hist: int

    def __str__(self):
        return (
            "Ticker = "
            + str(self.name)
            + " Last close price = "
            + str(self.lastcandle)
            + " EMA = "
            + str(self.ema)
            + " macdFast = "
            + str(self.macdfast)
            + " macdSlow = "
            + str(self.macdslow)
            + " hist = "
            + str(self.hist)
        )
