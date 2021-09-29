from abc import ABCMeta
from typing import List


class MenuComponent(metaclass=ABCMeta):
    def add(self, menu_component) -> None:
        raise RuntimeError()

    def remove(self, menu_component) -> None:
        raise RuntimeError()

    def get_child(self, i: int):
        raise RuntimeError()

    def get_name(self) -> str:
        raise RuntimeError()

    def get_description(self) -> str:
        raise RuntimeError()

    def get_price(self) -> float:
        raise RuntimeError()

    def is_vegetarian(self) -> bool:
        raise RuntimeError()

    def print(self) -> None:
        raise RuntimeError()


class Menu(MenuComponent):
    def __init__(self, name: str, description: str) -> None:
        self.name: str = name
        self.description: str = description
        self.menu_components: List[MenuComponent] = []

    def add(self, menu_component: MenuComponent) -> None:
        self.menu_components.append(menu_component)

    def remove(self, menu_component: MenuComponent) -> None:
        self.menu_components.remove(menu_component)

    def get_child(self, i: int) -> MenuComponent:
        return self.menu_components[i]

    def get_name(self) -> str:
        return self.name

    def get_description(self) -> str:
        return self.description

    def print(self) -> None:
        print(f'\n{self.get_name()}, {self.get_description()}---------------------')
        for menu_component in self.menu_components:
            menu_component.print()


class MenuItem(MenuComponent):
    def __init__(self, name: str, description: str, vegetarian: bool, price: float) -> None:
        self.name: str = name
        self.description: str = description
        self.vegetarian: bool = vegetarian
        self.price: float = price

    def get_name(self) -> str:
        return self.name

    def get_description(self) -> str:
        return self.description

    def get_price(self) -> float:
        return self.price

    def is_vegetarian(self) -> bool:
        return self.vegetarian

    def print(self) -> None:
        print(f"  {self.get_name()} {'(v)' if self.is_vegetarian() else ''}, {self.get_price()}")
        print(f"     -- {self.get_description()}")


class Waitress:
    def __init__(self, all_menus: MenuComponent) -> None:
        self.all_menus: MenuComponent = all_menus

    def print_menu(self) -> None:
        self.all_menus.print()


if __name__ == '__main__':
    pancake_house_menu: MenuComponent = Menu("PANCAKE HOUSE MENU", "Breakfast")
    diner_menu: MenuComponent = Menu("DINER MENU", "Lunch")
    cafe_menu: MenuComponent = Menu("CAFE MENU", "Dinner")
    dessert_menu: MenuComponent = Menu("DESSERT MENU", "Dessert of course!")
    coffee_menu: MenuComponent = Menu("COFFEE MENU", "Stuff to go with your afternoon coffee")

    all_menus: MenuComponent = Menu("ALL MENUS", "All menus combined")
    all_menus.add(pancake_house_menu)
    all_menus.add(diner_menu)
    all_menus.add(cafe_menu)

    pancake_house_menu.add(MenuItem("K&B's Pancake Breakfast", "Pancakes with scrambled eggs and toast", True, 2.99))
    pancake_house_menu.add(MenuItem("Regular Pancake Breakfast", "Pancakes with fried eggs, sausage", False, 2.99))
    pancake_house_menu.add(
        MenuItem("Blueberry Pancakes", "Pancakes made with fresh blueberries, and blueberry syrup", True, 3.49)
    )
    pancake_house_menu.add(MenuItem("Waffles", "Waffles with your choice of blueberries or strawberries", True, 3.59))

    diner_menu.add(MenuItem("Vegetarian BLT", "(Fakin') Bacon with lettuce & tomato on whole wheat", True, 2.99))
    diner_menu.add(MenuItem("BLT", "Bacon with lettuce & tomato on whole wheat", False, 2.99))
    diner_menu.add(
        MenuItem("Soup of the day", "A bowl of the soup of the day, with a side of potato salad", False, 3.29)
    )
    diner_menu.add(MenuItem("Hot Dog", "A hot dog, with saurkraut, relish, onions, topped with cheese", False, 3.05))
    diner_menu.add(MenuItem("Steamed Veggies and Brown Rice", "Steamed vegetables over brown rice", True, 3.99))
    diner_menu.add(MenuItem("Pasta", "Spaghetti with marinara sauce, and a slice of sourdough bread", True, 3.89))

    diner_menu.add(dessert_menu)

    dessert_menu.add(MenuItem("Apple Pie", "Apple pie with a flakey crust, topped with vanilla icecream", True, 1.59))
    dessert_menu.add(MenuItem("Cheesecake", "Creamy New York cheesecake, with a chocolate graham crust", True, 1.99))
    dessert_menu.add(MenuItem("Sorbet", "A scoop of raspberry and a scoop of lime", True, 1.89))

    cafe_menu.add(
        MenuItem(
            "Veggie Burger and Air Fries", "Veggie burger on a whole wheat bun, lettuce, tomato, and fries", True,
            3.99
        )
    )
    cafe_menu.add(MenuItem("Soup of the day", "A cup of the soup of the day, with a side salad", False, 3.69))
    cafe_menu.add(MenuItem("Burrito", "A large burrito, with whole pinto beans, salsa, guacamole", True, 4.29))

    cafe_menu.add(coffee_menu)

    coffee_menu.add(MenuItem("Coffee Cake", "Crumbly cake topped with cinnamon and walnuts", True, 1.59))
    coffee_menu.add(MenuItem("Bagel", "Flavors include sesame, poppyseed, cinnamon raisin, pumpkin", False, 0.69))
    coffee_menu.add(MenuItem("Biscotti", "Three almond or hazelnut biscotti cookies", True, 0.89))

    waitress: Waitress = Waitress(all_menus)

    waitress.print_menu()
