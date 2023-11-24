from typing import Protocol


class Exchange(Protocol):
    def get_prices(self, symbol: str) -> list[int]:
        raise NotImplementedError()

    def buy(self, symbol: str, amount: int) -> None:
        raise NotImplementedError()

    def sell(self, symbol: str, amount: int) -> None:
        raise NotImplementedError()
