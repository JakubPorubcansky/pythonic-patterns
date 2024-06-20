from dataclasses import dataclass, field
from typing import List


@dataclass
class Investor:
    name: str

    def notify(self, message: str):
        print(f"{self.name} received message: {message}")


@dataclass
class StockMarket:
    subscriptions: dict[str, List[Investor]] = field(default_factory=dict)

    def subscribe(self, investor: Investor, company: str):
        if not company in self.subscriptions:
            self.subscriptions[company] = []

        self.subscriptions[company].append(investor)

    def unsubscribe(self, investor: Investor, company: str):
        self.subscriptions[company].remove(investor)

    def issue_stock(self, company: str, amount: int):
        message = f"New stocks issued for {company}: {amount}"
        self.notify_investors(company, message)

    def announce_earnings_report(self, company: str, report: str):
        message = f"Earnings report for {company}: {report}"
        self.notify_investors(company, message)

    def notify_investors(self, company: str, message: str):
        if not company in self.subscriptions:
            return
        
        for investor in self.subscriptions[company]:
            investor.notify(message)

def main():
    # create stock market and investors
    stock_market = StockMarket()
    investor1 = Investor("Investor 1")
    investor2 = Investor("Investor 2")

    # subscribe investors to companies
    stock_market.subscribe(investor1, "Apple")
    stock_market.subscribe(investor2, "Apple")
    stock_market.subscribe(investor2, "Google")

    # issue new stocks for a company
    stock_market.issue_stock("Apple", 100)

    # announce earnings report for Google
    stock_market.announce_earnings_report(
    "Google", "Earnings report for Q4 2022: revenue $100B, profit $20B"
    )

    # unsubscribe an investor from a company
    stock_market.unsubscribe(investor2, "Apple")

    # announce earnings report for Apple
    stock_market.announce_earnings_report(
    "Apple", "Earnings report for Q4 2022: revenue $220B, profit $50B"
    )


if __name__ == "__main__":
    main()