from typing import List, Any
from abc import ABCMeta, abstractmethod


class Iterator(metaclass=ABCMeta):
    @abstractmethod
    def has_next(self) -> bool:
        raise NotImplementedError('`has_next method not implemented`')

    @abstractmethod
    def next(self) -> Any:
        raise NotImplementedError('`next method not implemented`')

    @abstractmethod
    def remove(self) -> None:
        raise NotImplementedError('`remove` method not implemented')


class Enumeration(metaclass=ABCMeta):
    @abstractmethod
    def has_more_elements(self) -> bool:
        raise NotImplementedError('`has_more_elements` method not implemented')

    @abstractmethod
    def next_element(self) -> Any:
        raise NotImplementedError('`next_element` method not implemented')


class EnumerationIterator(Iterator):
    def __init__(self, enumeration: Enumeration) -> None:
        self.enumeration: Enumeration = enumeration

    def has_next(self) -> bool:
        return self.enumeration.has_more_elements()

    def next(self) -> Any:
        return self.enumeration.next_element()

    def remove(self) -> None:
        raise NotImplementedError('`remove` method not implemented')


class IteratorEnumeration(Enumeration):
    def __init__(self, iterator: Iterator) -> None:
        self.iterator: Iterator = iterator

    def has_more_elements(self) -> bool:
        return self.iterator.has_next()

    def next_element(self) -> Any:
        return self.iterator.next()


class Vector:
    def __init__(self, items: List) -> None:
        self.items = items

    def has_more_elements(self) -> bool:
        return len(self.items) > 0

    def next_element(self) -> Any:
        return self.items.pop()

    def has_next(self) -> bool:
        return len(self.items) > 0

    def next(self) -> Any:
        return self.items.pop()


class EnumerationIteratorTestDrive:
    def __init__(self):
        v: Vector = Vector([1, 3, 4, 2, 5])
        iterator = EnumerationIterator(v)
        while iterator.has_next():
            print(iterator.next())


class IteratorEnumerationTestDrive:
    def __init__(self):
        v: Vector = Vector([3, 4, 5, 1, 2])
        enumeration = IteratorEnumeration(v)
        while enumeration.has_more_elements():
            print(enumeration.next_element())


if __name__ == '__main__':
    EnumerationIteratorTestDrive()
    IteratorEnumerationTestDrive()
