- Observer pattern
  - Mediator pattern (this is closer to event bus)
    - https://lostechies.com/derickbailey/2013/03/18/event-aggregator-andorvs-mediator-a-tale-of-two-patterns/
  - with event handler functions
  - when to use it: your functions do a lot of extra stuff that's not the responsibility of the function and don't affect the outcome that much

## Observer pattern diagram

```mermaid
classDiagram
    class Observer {
        <<abstract>>
        +notify()
    }
    class ConcreteObserver1 {
        +notify()
    }
    class ConcreteObserver2 {
        +notify()
    }
    ConcreteObserver1 --|> Observer
    ConcreteObserver2 --|> Observer
    Subject o-- Observer : notifies
    class Subject {
        observers: list[Observer]
        +registerObserver(observer)
        +unregisterObserver(observer)
        +notifyObservers()
    }
```

## Mediator

TODO: add Mediator diagram and example
