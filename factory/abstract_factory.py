from abc import ABCMeta, abstractmethod
from typing import List


class Dough(metaclass=ABCMeta):
    pass


class Sauce(metaclass=ABCMeta):
    pass


class Cheese(metaclass=ABCMeta):
    pass


class Veggies(metaclass=ABCMeta):
    pass


class Pepperoni(metaclass=ABCMeta):
    pass


class Clams(metaclass=ABCMeta):
    pass


class ThinCrustDough(Dough):
    def __str__(self):
        return 'Thin Crust Dough'


class ThickCrustDough(Dough):
    def __str__(self):
        return 'ThickCrust style extra thick crust dough'


class MarinaraSauce(Sauce):
    def __str__(self):
        return 'Marinara Sauce'


class PlumTomatoSauce(Sauce):
    def __str__(self):
        return 'Tomato sauce with plum tomatoes'


class ReggianoCheese(Cheese):
    def __str__(self):
        return 'Reggiano Cheese'


class MozzarellaCheese(Cheese):
    def __str__(self):
        return 'Shredded Mozzarella'


class Garlic(Veggies):
    def __str__(self):
        return 'Garlic'


class Onion(Veggies):
    def __str__(self):
        return 'Onion'


class Mushroom(Veggies):
    def __str__(self):
        return 'Mushrooms'


class RedPepper(Veggies):
    def __str__(self):
        return 'Red Pepper'


class BlackOlives(Veggies):
    def __str__(self):
        return 'Black Olives'


class Spinach(Veggies):
    def __str__(self):
        return 'Spinach'


class Eggplant(Veggies):
    def __str__(self):
        return 'Eggplant'


class SlicedPepperoni(Pepperoni):
    def __str__(self):
        return 'Sliced Pepperoni'


class FreshClams(Clams):
    def __str__(self):
        return 'Fresh Clams from Long Island Sound'


class FrozenClams(Clams):
    def __str__(self):
        return 'Frozen Clams from Chesapeake Bay'


class PizzaIngredientFactory(metaclass=ABCMeta):
    @abstractmethod
    def create_dough(self) -> Dough:
        raise NotImplementedError('create_dough method not implemented')

    @abstractmethod
    def create_sauce(self) -> Sauce:
        raise NotImplementedError('create_sauce method not implemented')

    @abstractmethod
    def create_cheese(self) -> Cheese:
        raise NotImplementedError('create_cheese method not implemented')

    @abstractmethod
    def create_veggies(self) -> List[Veggies]:
        raise NotImplementedError('create_veggies method not implemented')

    @abstractmethod
    def create_pepperoni(self) -> Pepperoni:
        raise NotImplementedError('create_pepperoni method not implemented')

    @abstractmethod
    def create_clam(self) -> Clams:
        raise NotImplementedError('create_clam method not implemented')


class NYPizzaIngredientFactory(PizzaIngredientFactory):

    def create_dough(self) -> Dough:
        return ThinCrustDough()

    def create_sauce(self) -> Sauce:
        return MarinaraSauce()

    def create_cheese(self) -> Cheese:
        return ReggianoCheese()

    def create_veggies(self) -> List[Veggies]:
        veggies = [Garlic(), Onion(), Mushroom(), RedPepper()]
        return veggies

    def create_pepperoni(self) -> Pepperoni:
        return SlicedPepperoni()

    def create_clam(self) -> Clams:
        return FreshClams()


class ChicagoPizzaIngredientFactory(PizzaIngredientFactory):
    def create_dough(self) -> Dough:
        return ThickCrustDough()

    def create_sauce(self) -> Sauce:
        return PlumTomatoSauce()

    def create_cheese(self) -> Cheese:
        return MozzarellaCheese()

    def create_veggies(self) -> List[Veggies]:
        veggies = [BlackOlives(), Spinach(), Eggplant()]
        return veggies

    def create_pepperoni(self) -> Pepperoni:
        return SlicedPepperoni()

    def create_clam(self) -> Clams:
        return FrozenClams()


class Pizza(metaclass=ABCMeta):
    def __init__(self) -> None:
        self.name = ''
        self.dough = None
        self.sauce = None
        self.veggies: List[Veggies] = []
        self.cheese = None
        self.pepperoni = None
        self.clam = None

    def set_name(self, name: str):
        self.name = name

    def get_name(self):
        return self.name

    @abstractmethod
    def prepare(self):
        raise NotImplementedError('prepare method not implemented')

    def bake(self):
        print('Bake for 25 minutes at 350')

    def cut(self):
        print('Cutting the pizza into diagonal slices')

    def box(self):
        print('Place pizza in official PizzaStore box')

    def __str__(self):
        display = ['name: ', self.name]
        if self.dough:
            display.append(str(self.dough))
        if self.sauce:
            display.append(str(self.sauce))
        if self.veggies:
            for i, j in enumerate(self.veggies):
                if i < len(self.veggies) - 1:
                    display.append(f'{str(j)}, ')
                else:
                    display.append(str(j))
        if self.clam:
            display.append(str(self.clam))
        if self.pepperoni:
            display.append(str(self.pepperoni))

        return '\n'.join(display)


class CheesePizza(Pizza):
    def __init__(self, ingredient_factory: PizzaIngredientFactory):
        self.ingredient_factory = ingredient_factory
        super(CheesePizza, self).__init__()

    def prepare(self):
        print(f'Preparing {self.name}')
        self.dough = self.ingredient_factory.create_dough()
        self.sauce = self.ingredient_factory.create_sauce()
        self.cheese = self.ingredient_factory.create_cheese()


class VeggiePizza(Pizza):
    def __init__(self, ingredient_factory: PizzaIngredientFactory):
        self.ingredient_factory = ingredient_factory
        super(VeggiePizza, self).__init__()

    def prepare(self):
        print(f'Preparing {self.name}')
        self.dough = self.ingredient_factory.create_dough()
        self.sauce = self.ingredient_factory.create_sauce()
        self.cheese = self.ingredient_factory.create_cheese()
        self.veggies = self.ingredient_factory.create_veggies()


class ClamPizza(Pizza):
    def __init__(self, ingredient_factory: PizzaIngredientFactory):
        self.ingredient_factory = ingredient_factory
        super(ClamPizza, self).__init__()

    def prepare(self):
        print(f'Preparing {self.name}')
        self.dough = self.ingredient_factory.create_dough()
        self.sauce = self.ingredient_factory.create_sauce()
        self.cheese = self.ingredient_factory.create_cheese()
        self.clam = self.ingredient_factory.create_clam()


class PepperoniPizza(Pizza):
    def __init__(self, ingredient_factory: PizzaIngredientFactory):
        self.ingredient_factory = ingredient_factory
        super(PepperoniPizza, self).__init__()

    def prepare(self):
        print(f'Preparing {self.name}')
        self.dough = self.ingredient_factory.create_dough()
        self.sauce = self.ingredient_factory.create_sauce()
        self.cheese = self.ingredient_factory.create_cheese()
        self.veggies = self.ingredient_factory.create_veggies()
        self.pepperoni = self.ingredient_factory.create_pepperoni()


class PizzaStore(metaclass=ABCMeta):
    @abstractmethod
    def create_pizza(self, item: str) -> Pizza:
        raise NotImplementedError('create_pizza method not implemented')

    def order_pizza(self, pizza_type: str) -> Pizza:
        pizza = self.create_pizza(pizza_type)
        print(f'--- Making a {pizza.get_name()} ---')
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        return pizza


class ChicagoPizzaStore(PizzaStore):
    def create_pizza(self, item: str) -> Pizza:
        ingredient_factory = ChicagoPizzaIngredientFactory()

        if item == 'cheese':
            pizza: Pizza = CheesePizza(ingredient_factory)
            pizza.set_name('Chicago Style Cheese Pizza')
        elif item == 'veggie':
            pizza = VeggiePizza(ingredient_factory)
            pizza.set_name('Chicago Style Veggie Pizza')
        elif item == 'clam':
            pizza = ClamPizza(ingredient_factory)
            pizza.set_name('Chicago Style Clam Pizza')
        elif item == 'pepperoni':
            pizza = PepperoniPizza(ingredient_factory)
            pizza.set_name('Chicago Style Pepperoni Pizza')
        else:
            raise Exception(f'no such kind pizza type: {item}')

        return pizza


class NYPizzaStore(PizzaStore):
    def create_pizza(self, item: str) -> Pizza:
        ingredient_factory = NYPizzaIngredientFactory()

        if item == 'cheese':
            pizza: Pizza = CheesePizza(ingredient_factory)
            pizza.set_name('New York Style Cheese Pizza')
        elif item == 'veggie':
            pizza = VeggiePizza(ingredient_factory)
            pizza.set_name('New York Style Veggie Pizza')
        elif item == 'clam':
            pizza = ClamPizza(ingredient_factory)
            pizza.set_name('New York Style Clam Pizza')
        elif item == 'pepperoni':
            pizza = PepperoniPizza(ingredient_factory)
            pizza.set_name('New York Style Pepperoni Pizza')
        else:
            raise Exception(f'no such kind pizza type: {item}')

        return pizza


if __name__ == '__main__':
    ny_store: PizzaStore = NYPizzaStore()
    chicago_store: PizzaStore = ChicagoPizzaStore()

    pizza: Pizza = ny_store.order_pizza('cheese')
    print(f'Ethan ordered a {pizza}\n')

    pizza = chicago_store.order_pizza('cheese')
    print(f'Joel ordered a {pizza}\n')

    pizza = ny_store.order_pizza('clam')
    print(f'Ethan ordered a {pizza}\n')

    pizza = chicago_store.order_pizza('clam')
    print(f'Joel ordered a {pizza}\n')

    pizza = ny_store.order_pizza('pepperoni')
    print(f'Ethan ordered a {pizza}\n')

    pizza = chicago_store.order_pizza('pepperoni')
    print(f'Joel ordered a {pizza}\n')

    pizza = ny_store.order_pizza('veggie')
    print(f'Ethan ordered a {pizza}\n')

    pizza = chicago_store.order_pizza('veggie')
    print(f'Joel ordered a {pizza}\n')
