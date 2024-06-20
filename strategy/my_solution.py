from dataclasses import dataclass
from typing import Callable

DiscountCalculator = Callable[[int, int], int]


def percentage_discount(price: int, quantity: int) -> int:
    return int(price * quantity * 0.20)


def fixed_discount(price: int, quantity: int) -> int:
    return 1000


@dataclass
class Order:
    price: int
    quantity: int
    discount_calculator: DiscountCalculator

    def compute_total(self) -> int:
        discount = self.discount_calculator(self.price, self.quantity)
        return self.price * self.quantity - discount


def main() -> None:
    order = Order(price=100_00, quantity=2, discount_calculator=percentage_discount)
    print(order)
    print(f"Total: ${order.compute_total()/100:.2f}")


if __name__ == "__main__":
    main()
