from abc import ABC, abstractmethod
from dataclasses import dataclass

from exchange import Exchange


@dataclass
class TradingBot(ABC):
    exchange: Exchange

    @abstractmethod
    def should_buy(self, symbol: str) -> bool:
        pass

    @abstractmethod
    def should_sell(self, symbol: str) -> bool:
        pass
