from abc import ABCMeta, abstractmethod


class Pizza(metaclass=ABCMeta):
    def __init__(self) -> None:
        self.description: str = 'Basic Pizza'

    def get_description(self) -> str:
        return self.description

    @abstractmethod
    def cost(self) -> float:
        raise NotImplementedError('`cost` method not implemented')


class ThickcrustPizza(Pizza):
    def __init__(self) -> None:
        self.description: str = 'Thick crust pizza, with tomato sauce'

    def cost(self) -> float:
        return 7.99


class ThincrustPizza(Pizza):
    def __init__(self) -> None:
        self.description: str = 'Thin crust pizza, with tomato sauce'

    def cost(self) -> float:
        return 7.99


class ToppingDecorator(Pizza):
    def __init__(self, pizza: Pizza) -> None:
        self.pizza: Pizza = pizza

    @abstractmethod
    def get_description(self) -> str:
        raise NotImplementedError('`get_description` method not implemented')


class Cheese(ToppingDecorator):
    def get_description(self) -> str:
        return f'{self.pizza.get_description()}, Cheese'

    def cost(self) -> float:
        return self.pizza.cost()


class Olives(ToppingDecorator):
    def get_description(self) -> str:
        return f'{self.pizza.get_description()}, Olives'

    def cost(self) -> float:
        return self.pizza.cost() + .3


if __name__ == '__main__':
    pizza: Pizza = ThincrustPizza()
    cheese_pizza: Pizza = Cheese(pizza)
    greek_pizza: Pizza = Olives(pizza)

    print(f'{greek_pizza.get_description()} ${greek_pizza.cost()}')
