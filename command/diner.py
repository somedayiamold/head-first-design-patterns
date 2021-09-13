from abc import ABCMeta, abstractmethod


class Order(metaclass=ABCMeta):
    @abstractmethod
    def order_up(self) -> None:
        raise NotImplementedError('`order_up` method not implemented')


class Cook:
    def make_burger(self) -> None:
        print('Making a burger')

    def make_fries(self) -> None:
        print('Making fries')


class BurgerAndFriesOrder(Order):
    def __init__(self, cook: Cook) -> None:
        self.cook: Cook = cook

    def order_up(self) -> None:
        self.cook.make_burger()
        self.cook.make_fries()


class Waitress:
    def take_order(self, order: Order) -> None:
        order.order_up()


class Customer:
    def __init__(self, waitress: Waitress) -> None:
        self.waitress: Waitress = waitress

    def create_order(self, order: Order) -> None:
        self.order = order

    def hungry(self) -> None:
        self.waitress.take_order(self.order)


class Diner:
    def __init__(self) -> None:
        cook: Cook = Cook()
        waitress: Waitress = Waitress()
        customer: Customer = Customer(waitress)
        customer.create_order(BurgerAndFriesOrder(cook))
        customer.hungry()


if __name__ == '__main__':
    Diner()
