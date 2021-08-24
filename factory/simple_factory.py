from typing import List


class Pizza():
    def __init__(self, name: str, dough: str, sauce: str, toppings: List[str]) -> None:
        self.name = name
        self.dough = dough
        self.sauce = sauce
        self.toppings = toppings

    def prepare(self):
        print(f'Preparing {self.name}')

    def bake(self):
        print(f'Baking {self.name}')

    def cut(self):
        print(f'Cutting {self.name}')

    def box(self):
        print(f'Boxing {self.name}')

    def __str__(self):
        display = ['name: ', self.name, self.dough, self.sauce, 'toppings: ']
        display.extend(self.toppings)
        return '\n'.join(display)


class CheesePizza(Pizza):
    def __init__(self) -> None:
        name = 'Cheese Pizza'
        dough = 'Regular Crust'
        sauce = 'Marinara Pizza Sauce'
        toppings = ['Fresh Mozzarella', 'Parmesan']
        super(CheesePizza, self).__init__(name, dough, sauce, toppings)


class PepperoniPizza(Pizza):
    def __init__(self) -> None:
        name = 'Pepperoni Pizza'
        dough = 'Crust'
        sauce = 'Marinara Pizza Sauce'
        toppings = ['Sliced Pepperoni', 'Sliced Onion', 'Grated parmesan cheese']
        super(PepperoniPizza, self).__init__(name, dough, sauce, toppings)


class ClamPizza(Pizza):
    def __init__(self) -> None:
        name = 'Pepperoni Pizza'
        dough = 'Crust'
        sauce = 'Marinara sauce'
        toppings = ['Clams', 'Grated parmesan cheese']
        super(ClamPizza, self).__init__(name, dough, sauce, toppings)


class VeggiePizza(Pizza):
    def __init__(self) -> None:
        name = 'Veggie Pizza'
        dough = 'Crust'
        sauce = 'Marinara sauce'
        toppings = [
            'Shredded mozzarella', 'Grated parmesan', 'Diced onion', 'Sliced mushrooms', 'Sliced red pepper',
            'Sliced black olives'
        ]
        super(VeggiePizza, self).__init__(name, dough, sauce, toppings)


class SimplePizzaFactory():
    @staticmethod
    def create_pizza(pizza_type: str) -> Pizza:
        if pizza_type == 'cheese':
            return CheesePizza()
        elif pizza_type == 'pepperoni':
            return PepperoniPizza()
        elif pizza_type == 'clam':
            return ClamPizza()
        elif pizza_type == 'veggie':
            return VeggiePizza()
        else:
            raise Exception(f'no such kind pizza type: {pizza_type}')


class PizzaStore():
    def __init__(self, factory) -> None:
        self.factory = factory

    def order_pizza(self, pizza_type: str):
        pizza = self.factory.create_pizza(pizza_type)
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()


if __name__ == '__main__':
    factory = SimplePizzaFactory
    store = PizzaStore(factory)
    store.order_pizza('cheese')
    store.order_pizza('veggie')
    store.order_pizza('xxx')
