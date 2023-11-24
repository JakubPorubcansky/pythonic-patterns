from dataclasses import dataclass
from typing import Protocol


@dataclass
class TradingBot(Protocol):
    def should_buy(self, symbol: str) -> bool:
        raise NotImplementedError()

    def should_sell(self, symbol: str) -> bool:
        raise NotImplementedError()
