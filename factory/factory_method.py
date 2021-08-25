from abc import ABCMeta, abstractmethod
from typing import List


class Pizza:
    def __init__(self, name: str, dough: str, sauce: str, toppings: List[str]) -> None:
        self.name = name
        self.dough = dough
        self.sauce = sauce
        self.toppings = toppings

    def get_name(self):
        return self.name

    def prepare(self):
        print(f'Preparing {self.name}')
        print('Tossing dough...')
        print('Adding sauce...')
        print('Adding toppings: ')
        for topping in self.toppings:
            print(f'    {topping}')

    def bake(self):
        print('Bake for 25 minutes at 350')

    def cut(self):
        print('Cutting the pizza into diagonal slices')

    def box(self):
        print('Place pizza in official PizzaStore box')

    def __str__(self):
        display = ['name: ', self.name, self.dough, self.sauce, 'toppings: ']
        display.extend(self.toppings)
        return '\n'.join(display)


class PizzaStore:
    __metaclass__ = ABCMeta

    @abstractmethod
    def create_pizza(self, pizza_type: str) -> Pizza:
        raise NotImplementedError('create_pizza method not implemented')

    def order_pizza(self, pizza_type: str) -> Pizza:
        pizza = self.create_pizza(pizza_type)
        print(f'--- Making a {pizza.get_name()} ---')
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        return pizza


class ChicagoStyleCheesePizza(Pizza):
    def __init__(self) -> None:
        name = 'Chicago Style Deep Dish Cheese Pizza'
        dough = 'Extra Thick Crust Dough'
        sauce = 'Plum Tomato Sauce'
        toppings = ['Shredded Mozzarella Cheese']
        super(ChicagoStyleCheesePizza, self).__init__(name, dough, sauce, toppings)

    def cut(self):
        print('Cutting the pizza into square slices')


class ChicagoStyleVeggiePizza(Pizza):
    def __init__(self) -> None:
        name = 'Chicago Deep Dish Veggie Pizza'
        dough = 'Extra Thick Crust Dough'
        sauce = 'Plum Tomato Sauce'
        toppings = ['Shredded Mozzarella Cheese', 'Black Olives', 'Spinach', 'Eggplant']
        super(ChicagoStyleVeggiePizza, self).__init__(name, dough, sauce, toppings)

    def cut(self):
        print('Cutting the pizza into square slices')


class ChicagoStyleClamPizza(Pizza):
    def __init__(self) -> None:
        name = 'Chicago Style Clam Pizza'
        dough = 'Extra Thick Crust Dough'
        sauce = 'Plum Tomato Sauce'
        toppings = ['Shredded Mozzarella Cheese', 'Frozen Clams from Chesapeake Bay']
        super(ChicagoStyleClamPizza, self).__init__(name, dough, sauce, toppings)

    def cut(self):
        print('Cutting the pizza into square slices')


class ChicagoStylePepperoniPizza(Pizza):
    def __init__(self) -> None:
        name = 'Chicago Style Pepperoni Pizza'
        dough = 'Extra Thick Crust Dough'
        sauce = 'Plum Tomato Sauce'
        toppings = ['Shredded Mozzarella Cheese', 'Black Olives', 'Spinach', 'Eggplant', 'Sliced Pepperoni']
        super(ChicagoStylePepperoniPizza, self).__init__(name, dough, sauce, toppings)

    def cut(self):
        print('Cutting the pizza into square slices')


class NYStyleCheesePizza(Pizza):
    def __init__(self) -> None:
        name = 'NY Style Sauce and Cheese Pizza'
        dough = 'Thin Crust Dough'
        sauce = 'Marinara Sauce'
        toppings = ['Grated Reggiano Cheese']
        super(NYStyleCheesePizza, self).__init__(name, dough, sauce, toppings)


class NYStyleVeggiePizza(Pizza):
    def __init__(self) -> None:
        name = 'NY Style Veggie Pizza'
        dough = 'Thin Crust Dough'
        sauce = 'Marinara Sauce'
        toppings = ['Grated Reggiano Cheese', 'Garlic', 'Onion', 'Mushrooms', 'Red Pepper']
        super(NYStyleVeggiePizza, self).__init__(name, dough, sauce, toppings)


class NYStyleClamPizza(Pizza):
    def __init__(self) -> None:
        name = 'NY Style Clam Pizza'
        dough = 'Thin Crust Dough'
        sauce = 'Marinara Sauce'
        toppings = ['Grated Reggiano Cheese', 'Fresh Clams from Long Island Sound']
        super(NYStyleClamPizza, self).__init__(name, dough, sauce, toppings)


class NYStylePepperoniPizza(Pizza):
    def __init__(self) -> None:
        name = 'NY Style Pepperoni Pizza'
        dough = 'Thin Crust Dough'
        sauce = 'Marinara Sauce'
        toppings = ['Grated Reggiano Cheese', 'Sliced Pepperoni', 'Garlic', 'Onion', 'Mushrooms', 'Red Pepper']
        super(NYStylePepperoniPizza, self).__init__(name, dough, sauce, toppings)


class ChicagoPizzaStore(PizzaStore):
    def create_pizza(self, pizza_type: str):
        if pizza_type == 'cheese':
            return ChicagoStyleCheesePizza()
        elif pizza_type == 'veggie':
            return ChicagoStyleVeggiePizza()
        elif pizza_type == 'clam':
            return ChicagoStyleClamPizza()
        elif pizza_type == 'pepperoni':
            return ChicagoStylePepperoniPizza()
        else:
            raise Exception(f'no such kind pizza type: {pizza_type}')


class NYPizzaStore(PizzaStore):
    def create_pizza(self, pizza_type: str):
        if pizza_type == 'cheese':
            return NYStyleCheesePizza()
        elif pizza_type == 'veggie':
            return NYStyleVeggiePizza()
        elif pizza_type == 'clam':
            return NYStyleClamPizza()
        elif pizza_type == 'pepperoni':
            return NYStylePepperoniPizza()
        else:
            raise Exception(f'no such kind pizza type: {pizza_type}')


class DependentPizzaStore:
    def __init__(self):
        pass

    def create_pizza(self, style: str, pizza_type: str):
        if style == 'NY':
            if pizza_type == 'cheese':
                pizza: Pizza = NYStyleCheesePizza()
            elif pizza_type == 'veggie':
                pizza = NYStyleVeggiePizza()
            elif pizza_type == 'clam':
                pizza = NYStyleClamPizza()
            elif pizza_type == 'pepperoni':
                pizza = NYStylePepperoniPizza()
            else:
                raise Exception(f'no such kind pizza type: {pizza_type}')
        elif style == 'Chicago':
            if pizza_type == 'cheese':
                pizza = ChicagoStyleCheesePizza()
            elif pizza_type == 'veggie':
                pizza = ChicagoStyleVeggiePizza()
            elif pizza_type == 'clam':
                pizza = ChicagoStyleClamPizza()
            elif pizza_type == 'pepperoni':
                pizza = ChicagoStylePepperoniPizza()
            else:
                raise Exception(f'no such kind pizza type: {pizza_type}')
        else:
            print('Error: invalid type of pizza')

        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()


if __name__ == '__main__':
    ny_store: PizzaStore = NYPizzaStore()
    chicago_store: PizzaStore = ChicagoPizzaStore()

    pizza: Pizza = ny_store.order_pizza('cheese')
    print(f'Ethan ordered a {pizza.get_name()}\n')

    pizza = chicago_store.order_pizza('cheese')
    print(f'Joel ordered a {pizza.get_name()}\n')

    pizza = ny_store.order_pizza('clam')
    print(f'Ethan ordered a {pizza.get_name()}\n')

    pizza = chicago_store.order_pizza('clam')
    print(f'Joel ordered a {pizza.get_name()}\n')

    pizza = ny_store.order_pizza('pepperoni')
    print(f'Ethan ordered a {pizza.get_name()}\n')

    pizza = chicago_store.order_pizza('pepperoni')
    print(f'Joel ordered a {pizza.get_name()}\n')

    pizza = ny_store.order_pizza('veggie')
    print(f'Ethan ordered a {pizza.get_name()}\n')

    pizza = chicago_store.order_pizza('veggie')
    print(f'Joel ordered a {pizza.get_name()}\n')
