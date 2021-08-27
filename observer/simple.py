from abc import ABCMeta, abstractmethod
from typing import List


class Observer:
    __metaclass__ = ABCMeta

    @abstractmethod
    def update(self, value: int) -> None:
        raise NotImplementedError('`update` method not implemented')


class Subject:
    __metaclass__ = ABCMeta

    @abstractmethod
    def register_observer(self, o: Observer) -> None:
        raise NotImplementedError('`register_observer` method not implemented')

    @abstractmethod
    def remove_observer(self, o: Observer) -> None:
        raise NotImplementedError('`remove_observer` method not implemented')

    @abstractmethod
    def notify_observers(self) -> None:
        raise NotImplementedError('`remove_observer` method not implemented')


class SimpleSubject(Subject):
    def __init__(self) -> None:
        self._observers: List[Observer] = []
        self._value: int = 0

    def register_observer(self, o: Observer) -> None:
        self._observers.append(o)

    def remove_observer(self, o: Observer) -> None:
        self._observers.remove(o)

    def notify_observers(self) -> None:
        for observer in self._observers:
            observer.update(self._value)

    def set_value(self, value: int) -> None:
        self._value = value
        self.notify_observers()


class SimpleObserver(Observer):
    def __init__(self, simple_subject: SimpleSubject):
        self._value: int
        self._simple_subject: Subject = simple_subject
        self._simple_subject.register_observer(self)

    def update(self, value: int) -> None:
        self._value = value
        self.display()

    def display(self) -> None:
        print(f'Value: {self._value}')


if __name__ == '__main__':
    simple_subject: SimpleSubject = SimpleSubject()
    simple_observer: SimpleObserver = SimpleObserver(simple_subject)
    simple_subject.set_value(80)
    simple_subject.remove_observer(simple_observer)
