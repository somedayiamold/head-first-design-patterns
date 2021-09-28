from abc import ABCMeta, abstractmethod
from collections.abc import Iterable
from typing import List, Dict


class MenuItem:
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

    def __str__(self) -> str:
        return f'{self.name}, ${self.price}\n   {self.description}'


class Menu(metaclass=ABCMeta):
    @abstractmethod
    def create_iterator(self) -> Iterable[MenuItem]:
        raise NotImplementedError('`create_iterator` method not implemented')


class DinerMenuIterator:
    def __init__(self, items: List[MenuItem]) -> None:
        self.items: List[MenuItem] = items
        self.position: int = 0

    def __iter__(self):
        return self

    def __next__(self) -> MenuItem:
        if self.position > len(self.items) - 1:
            raise StopIteration()
        menu_item: MenuItem = self.items[self.position]
        self.position += 1
        return menu_item


class DinerMenu(Menu):
    MAX_ITEMS: int = 6

    def __init__(self) -> None:
        self.menu_items: List[MenuItem] = [None] * self.MAX_ITEMS
        self.number_of_items: int = 0

        self.add_item("Vegetarian BLT", "(Fakin') Bacon with lettuce & tomato on whole wheat", True, 2.99)
        self.add_item("BLT", "Bacon with lettuce & tomato on whole wheat", False, 2.99)
        self.add_item("Soup of the day", "Soup of the day, with a side of potato salad", False, 3.29)
        self.add_item("Hotdog", "A hot dog, with sauerkraut, relish, onions, topped with cheese", False, 3.05)
        self.add_item("Steamed Veggies and Brown Rice", "Steamed vegetables over brown rice", True, 3.99)
        self.add_item("Pasta", "Spaghetti with Marinara Sauce, and a slice of sourdough bread", True, 3.89)

    def add_item(self, name: str, description: str, vegetarian: bool, price: float) -> None:
        menu_item: MenuItem = MenuItem(name, description, vegetarian, price)
        if self.number_of_items >= self.MAX_ITEMS:
            print("Sorry, menu is full!  Can't add item to menu")
        else:
            self.menu_items[self.number_of_items] = menu_item
            self.number_of_items += 1

    def get_menu_items(self) -> List[MenuItem]:
        return self.menu_items

    def create_iterator(self) -> Iterable[MenuItem]:
        return DinerMenuIterator(self.menu_items)


class PancakeHouseMenuIterator:
    def __init__(self, items: List[MenuItem]) -> None:
        self.items: List[MenuItem] = items
        self.position: int = 0

    def __iter__(self):
        return self

    def __next__(self) -> MenuItem:
        if self.position > len(self.items) - 1:
            raise StopIteration()
        menu_item: MenuItem = self.items[self.position]
        self.position += 1
        return menu_item


class PancakeHouseMenu(Menu):
    def __init__(self) -> None:
        self.menu_items: List[MenuItem] = []
        self.add_item("K&B's Pancake Breakfast", "Pancakes with scrambled eggs and toast", True, 2.99)
        self.add_item("Regular Pancake Breakfast", "Pancakes with fried eggs, sausage", False, 2.99)
        self.add_item("Blueberry Pancakes", "Pancakes made with fresh blueberries", True, 3.49)
        self.add_item("Waffles", "Waffles with your choice of blueberries or strawberries", True, 3.59)

    def add_item(self, name: str, description: str, vegetarian: bool, price: float) -> None:
        menu_item: MenuItem = MenuItem(name, description, vegetarian, price)
        self.menu_items.append(menu_item)

    def get_menu_items(self) -> List[MenuItem]:
        return self.menu_items

    def create_iterator(self) -> Iterable[MenuItem]:
        return PancakeHouseMenuIterator(self.menu_items)

    def __str__(self) -> str:
        return "Objectville Pancake House Menu"


class CafeMenu(Menu):
    def __init__(self) -> None:
        self.menu_items: Dict[str, MenuItem] = dict()
        self.add_item(
            "Veggie Burger and Air Fries", "Veggie burger on a whole wheat bun, lettuce, tomato, and fries", True, 3.99
        )
        self.add_item("Soup of the day", "A cup of the soup of the day, with a side salad", False, 3.69)
        self.add_item("Burrito", "A large burrito, with whole pinto beans, salsa, guacamole", True, 4.29)

    def add_item(self, name: str, description: str, vegetarian: bool, price: float) -> None:
        menu_item: MenuItem = MenuItem(name, description, vegetarian, price)
        self.menu_items.update({name: menu_item})

    def get_menu_items(self) -> Dict[str, MenuItem]:
        return self.menu_items

    def create_iterator(self) -> Iterable[MenuItem]:
        for menu_item in self.menu_items.values():
            yield menu_item


class Waitress:
    def __init__(self, pancake_house_menu: Menu, diner_menu: Menu, cafe_menu: Menu) -> None:
        self.pancake_house_menu: Menu = pancake_house_menu
        self.diner_menu: Menu = diner_menu
        self.cafe_menu: Menu = cafe_menu

    def print_menu(self) -> None:
        pancake_iterator: Iterable[MenuItem] = self.pancake_house_menu.create_iterator()
        diner_iterator: Iterable[MenuItem] = self.diner_menu.create_iterator()
        cafe_iterator: Iterable[MenuItem] = self.cafe_menu.create_iterator()

        print("MENU\n----\nBREAKFAST")
        self._print_menu(pancake_iterator)
        print("\nLUNCH")
        self._print_menu(diner_iterator)
        print("\nDINNER")
        self._print_menu(cafe_iterator)

    def _print_menu(self, iterator: Iterable[MenuItem]) -> None:
        for menu_item in iterator:
            print(f'{menu_item.get_name()}, {menu_item.get_price()} -- {menu_item.get_description()}')

    def print_vegetarian_menu(self) -> None:
        print("\nVEGETARIAN MENU\n---------------")
        self._print_vegetarian_menu(self.pancake_house_menu.create_iterator())
        self._print_vegetarian_menu(self.diner_menu.create_iterator())
        self._print_vegetarian_menu(self.cafe_menu.create_iterator())

    def is_item_vegetarian(self, name: str) -> bool:
        breakfast_iterator: Iterable[MenuItem] = self.pancake_house_menu.create_iterator()
        if self._is_vegetarian(name, breakfast_iterator):
            return True
        diner_iterator: Iterable[MenuItem] = self.diner_menu.create_iterator()
        if self._is_vegetarian(name, diner_iterator):
            return True
        cafe_iterator: Iterable[MenuItem] = self.cafe_menu.create_iterator()
        if self._is_vegetarian(name, cafe_iterator):
            return True
        return False

    def _print_vegetarian_menu(self, iterator: Iterable[MenuItem]) -> None:
        for menu_item in iterator:
            if menu_item.is_vegetarian():
                print(f'{menu_item.get_name()}, {menu_item.get_price()} -- {menu_item.get_description()}')

    def _is_vegetarian(self, name: str, iterator: Iterable[MenuItem]) -> bool:
        for menu_item in iterator:
            if menu_item.get_name() == name:
                if menu_item.is_vegetarian():
                    return True
        return False


if __name__ == '__main__':
    pancake_house_menu: PancakeHouseMenu = PancakeHouseMenu()
    diner_menu: DinerMenu = DinerMenu()
    cafe_menu: CafeMenu = CafeMenu()

    waitress: Waitress = Waitress(pancake_house_menu, diner_menu, cafe_menu)
    waitress.print_menu()
    waitress.print_vegetarian_menu()

    print("\nCustomer asks, is the Hotdog vegetarian?")
    print("Waitress says: ")
    if waitress.is_item_vegetarian("Hotdog"):
        print("Yes")
    else:
        print("No")
    print("\nCustomer asks, are the Waffles vegetarian?")
    print("Waitress says: ")
    if waitress.is_item_vegetarian("Waffles"):
        print("Yes")
    else:
        print("No")
