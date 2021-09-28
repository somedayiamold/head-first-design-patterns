from abc import ABCMeta, abstractmethod
from collections.abc import Iterable
from typing import List


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


class Iterator(metaclass=ABCMeta):
    @abstractmethod
    def has_next(self) -> bool:
        raise NotImplementedError('`has_next` method not implemented')

    @abstractmethod
    def next(self) -> MenuItem:
        raise NotImplementedError('`next` method not implemented')


class Menu(metaclass=ABCMeta):
    @abstractmethod
    def create_iterator(self) -> Iterator:
        raise NotImplementedError('`create_iterator` method not implemented')


class DinerMenuIterator(Iterator):
    def __init__(self, items: List[MenuItem]) -> None:
        self.items: List[MenuItem] = items
        self.position: int = 0

    def next(self) -> MenuItem:
        menu_item: MenuItem = self.items[self.position]
        self.position += 1
        return menu_item

    def has_next(self) -> bool:
        return len(self.items) > self.position


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

    def create_iterator(self) -> Iterator:
        return DinerMenuIterator(self.menu_items)


class PancakeHouseMenuIterator(Iterator):
    def __init__(self, items: List[MenuItem]) -> None:
        self.items: List[MenuItem] = items
        self.position: int = 0

    def next(self) -> MenuItem:
        menu_item: MenuItem = self.items[self.position]
        self.position += 1
        return menu_item

    def has_next(self) -> bool:
        return len(self.items) > self.position


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

    def create_iterator(self) -> Iterator:
        return PancakeHouseMenuIterator(self.menu_items)

    def __str__(self) -> str:
        return "Objectville Pancake House Menu"


class Waitress:
    def __init__(self, pancake_house_menu: Menu, diner_menu: Menu) -> None:
        self.pancake_house_menu: Menu = pancake_house_menu
        self.diner_menu: Menu = diner_menu

    def print_menu(self) -> None:
        pancake_iterator: Iterator = self.pancake_house_menu.create_iterator()
        diner_iterator: Iterator = self.diner_menu.create_iterator()

        print("MENU\n----\nBREAKFAST")
        self._print_menu(pancake_iterator)
        print("\nLUNCH")
        self._print_menu(diner_iterator)

    def _print_menu(self, iterator: Iterator) -> None:
        while iterator.has_next():
            menu_item: MenuItem = iterator.next()
            print(f'{menu_item.get_name()}, {menu_item.get_price()} -- {menu_item.get_description()}')

    def print_vegetarian_menu(self) -> None:
        self._print_vegetarian_menu(self.pancake_house_menu.create_iterator())
        self._print_vegetarian_menu(self.diner_menu.create_iterator())

    def is_item_vegetarian(self, name: str) -> bool:
        breakfast_iterator: Iterator = self.pancake_house_menu.create_iterator()
        if self._is_vegetarian(name, breakfast_iterator):
            return True
        diner_iterator: Iterator = self.diner_menu.create_iterator()
        if self._is_vegetarian(name, diner_iterator):
            return True
        return False

    def _print_vegetarian_menu(self, iterator: Iterator) -> None:
        while iterator.has_next():
            menu_item: MenuItem = iterator.next()
            if menu_item.is_vegetarian():
                print(f'{menu_item.get_name()},\t\t{menu_item.get_price()}\t{menu_item.get_description()}')

    def _is_vegetarian(self, name: str, iterator: Iterator) -> bool:
        while iterator.has_next():
            menu_item: MenuItem = iterator.next()
            if menu_item.get_name() == name:
                if menu_item.is_vegetarian():
                    return True
        return False


class MenuTestDrive:
    def __init__(self) -> None:
        pancake_house_menu: Menu = PancakeHouseMenu()
        diner_menu: Menu = DinerMenu()

        waitress: Waitress = Waitress(pancake_house_menu, diner_menu)
        waitress.print_menu()

        self.print_menus()

    def print_menus(self) -> None:
        pancake_house_menu: PancakeHouseMenu = PancakeHouseMenu()
        diner_menu: DinerMenu = DinerMenu()

        breakfast_items: List[MenuItem] = pancake_house_menu.get_menu_items()
        lunch_items: List[MenuItem] = diner_menu.get_menu_items()

        self.print_menu(breakfast_items)
        self.print_menu(lunch_items)

        print("=== forEach ===")
        for item in breakfast_items:
            print(item)
        for item in lunch_items:
            print(item)
        print("=== forEach ===")

        print("USING ENHANCED FOR")
        for menu_item in breakfast_items:
            print(f'{menu_item.get_name()}\t\t{menu_item.get_price()}\t{menu_item.get_description()}')
        for menu_item in lunch_items:
            print(f'{menu_item.get_name()}\t\t{menu_item.get_price()}\t{menu_item.get_description()}')

        print("USING FOR LOOPS")
        for i in range(len(breakfast_items)):
            menu_item = breakfast_items[i]
            print(f'{menu_item.get_name()}\t\t{menu_item.get_price()}\t{menu_item.get_description()}')

        for i in range(len(lunch_items)):
            menu_item = lunch_items[i]
            print(f'{menu_item.get_name()}\t\t{menu_item.get_price()}\t{menu_item.get_description()}')

    def print_menu(self, a: Iterable[MenuItem]) -> None:
        for menu_item in a:
            print(f'{menu_item.get_name()}\t\t{menu_item.get_price()}\t{menu_item.get_description()}')


if __name__ == '__main__':
    MenuTestDrive()
