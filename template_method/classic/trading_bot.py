from abc import ABC, abstractmethod


class TradingBot(ABC):
    @abstractmethod
    def buy(self, amount: int) -> None:
        pass

    @abstractmethod
    def sell(self, amount: int) -> None:
        pass

    @abstractmethod
    def should_buy(self, prices: list[int]) -> bool:
        pass

    @abstractmethod
    def should_sell(self, prices: list[int]) -> bool:
        pass

    @abstractmethod
    def get_price_data(self) -> list[int]:
        pass

    @abstractmethod
    def get_amount(self) -> int:
        pass

    def trade(self) -> None:
        prices = self.get_price_data()
        amount = self.get_amount()

        if self.should_buy(prices):
            self.buy(amount)
        if self.should_sell(prices):
            self.sell(amount)
