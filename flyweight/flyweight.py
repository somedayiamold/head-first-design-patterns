import traceback
from abc import ABCMeta, abstractmethod
from typing import List, Tuple
from datetime import datetime


class Tree(metaclass=ABCMeta):
    @abstractmethod
    def display(self, x: int, y: int) -> None:
        raise NotImplementedError('`display` method not implemented')

    def is_within_range(self, a_date) -> bool:
        return a_date.month > 2 and a_date.month < 11


class DeciduousTree(Tree):
    def display(self, x: int, y: int) -> None:
        print(f'Deciduous tree is located at {x}, {y}')
        if not self.is_within_range(datetime.now()):
            print('The tree currently has no leaves')


class ConiferTree(Tree):
    def display(self, x: int, y: int) -> None:
        print(f'Conifer tree is located at {x}, {y}')


class TreeFactory:
    def __init__(self) -> None:
        self.d = DeciduousTree()
        self.c = ConiferTree()

    def get_tree(self, _type: str) -> Tree:
        if _type == 'deciduous':
            return self.d
        elif _type == 'conifer':
            return self.c
        else:
            raise Exception('Invalid kind of tree')


if __name__ == '__main__':
    deciduous_locations: List[Tuple[int, int]] = [(1, 1), (33, 50), (100, 90)]
    conifer_locations: List[Tuple[int, int]] = [(10, 87), (24, 76), (2, 64)]
    tree_factory: TreeFactory = TreeFactory()
    try:
        d = tree_factory.get_tree('deciduous')
        c = tree_factory.get_tree('conifer')
        for location in deciduous_locations:
            d.display(location[0], location[1])
        for location in conifer_locations:
            c.display(location[0], location[1])
    except Exception:
        print(traceback.format_exc())
