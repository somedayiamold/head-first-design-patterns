from abc import ABCMeta, abstractmethod


class Beverage(metaclass=ABCMeta):
    def __init__(self) -> None:
        self.description = 'Unknown Beverage'

    def get_description(self) -> str:
        return self.description

    @abstractmethod
    def cost(self) -> float:
        raise NotImplementedError('`cost` method not implemented')


class CondimentDecorator(Beverage):
    def __init__(self, beverage: Beverage) -> None:
        self.beverage: Beverage = beverage

    @abstractmethod
    def get_description(self) -> str:
        raise NotImplementedError('`get_description` method not implemented')


class DarkRoast(Beverage):
    def __init__(self) -> None:
        self.description = 'Dark Roast Coffee'

    def cost(self) -> float:
        return .99


class Decaf(Beverage):
    def __init__(self) -> None:
        self.description = 'Decaf Coffee'

    def cost(self) -> float:
        return 1.05


class Espresso(Beverage):
    def __init__(self) -> None:
        self.description = 'Espresso'

    def cost(self) -> float:
        return 1.99


class HouseBlend(Beverage):
    def __init__(self) -> None:
        self.description = 'House Blend Coffee'

    def cost(self) -> float:
        return .89


class Milk(CondimentDecorator):
    def get_description(self) -> str:
        return f'{self.beverage.get_description()}, Milk'

    def cost(self) -> float:
        return 0.10 + self.beverage.cost()


class Mocha(CondimentDecorator):
    def get_description(self) -> str:
        return f'{self.beverage.get_description()}, Mocha'

    def cost(self) -> float:
        return 0.20 + self.beverage.cost()


class Soy(CondimentDecorator):
    def get_description(self) -> str:
        return f'{self.beverage.get_description()}, Soy'

    def cost(self) -> float:
        return 0.15 + self.beverage.cost()


class Whip(CondimentDecorator):
    def get_description(self) -> str:
        return f'{self.beverage.get_description()}, Whip'

    def cost(self) -> float:
        return 0.10 + self.beverage.cost()


if __name__ == '__main__':
    beverage: Beverage = Espresso()
    print(f'{beverage.get_description()} ${beverage.cost()}')

    beverage2: Beverage = DarkRoast()
    beverage2 = Mocha(beverage2)
    beverage2 = Mocha(beverage2)
    beverage2 = Whip(beverage2)
    print(f'{beverage2.get_description()} ${beverage2.cost()}')

    beverage3: Beverage = HouseBlend()
    beverage3 = Soy(beverage3)
    beverage3 = Mocha(beverage3)
    beverage3 = Whip(beverage3)
    print(f'{beverage3.get_description()} ${beverage3.cost()}')
