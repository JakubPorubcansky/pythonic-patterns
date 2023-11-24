# Strategy pattern diagrams

```mermaid
classDiagram
    class Context {

    }
    class Strategy {
        <<interface>>
        execute()
    }
    class ConcreteStrategyA {
        execute()
    }
    class ConcreteStrategyB {
        execute()
    }
    Strategy <|-- ConcreteStrategyA
    Strategy <|-- ConcreteStrategyB
    Context *-- Strategy
```

```mermaid
classDiagram
    class Main {

    }
    class DiscountStrategy {
        <<interface>>
        +int compute(int price)
    }
    class PercentageDiscount {
        +int compute(int price)
    }
    class FixedDiscount {
        +int compute(int price)
    }
    DiscountStrategy <|-- PercentageDiscount
    DiscountStrategy <|-- FixedDiscount
    Main *-- DiscountStrategy
```

- Explain the before version:
  - If-else statement that might become complex if more discount types are added
  - Magic numbers
- Classic strategy pattern:
  - We use ABC and inheritance
  - Still magic numbers in the strategy
- Now show functional version
- Another variant: callable (basically means removing the naming)
  - And move the magic numbers to instance variables
- How to do that in the functional scenario? Possibility: closures
- Another option: partial function application
