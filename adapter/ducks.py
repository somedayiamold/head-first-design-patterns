import random
from abc import ABCMeta, abstractmethod


class Duck(metaclass=ABCMeta):
    @abstractmethod
    def quack(self) -> None:
        raise NotImplementedError('`quack` method not implemented')

    @abstractmethod
    def fly(self) -> None:
        raise NotImplementedError('`fly` method not implemented')


class Turkey(metaclass=ABCMeta):
    @abstractmethod
    def gobble(self) -> None:
        raise NotImplementedError('`gobble` method not implemented')

    @abstractmethod
    def fly(self) -> None:
        raise NotImplementedError('`fly` method not implemented')


class Drone(metaclass=ABCMeta):
    @abstractmethod
    def beep(self) -> None:
        raise NotImplementedError('`beep` method not implemented')

    @abstractmethod
    def spin_rotors(self) -> None:
        raise NotImplementedError('`spin_rotors` method not implemented')

    @abstractmethod
    def take_off(self) -> None:
        raise NotImplementedError('`take_off` method not implemented')


class MallardDuck(Duck):
    def quack(self) -> None:
        print("Quack")

    def fly(self) -> None:
        print("I'm flying")


class WildTurkey(Turkey):
    def gobble(self) -> None:
        print("Gobble gobble")

    def fly(self) -> None:
        print("I'm flying a short distance")


class SuperDrone(Drone):
    def beep(self) -> None:
        print("Beep beep beep")

    def spin_rotors(self) -> None:
        print("Rotors are spinning")

    def take_off(self) -> None:
        print("Taking off")


class DuckAdapter(Turkey):
    def __init__(self, duck: Duck) -> None:
        self.duck: Duck = duck
        self.rand = random

    def gobble(self) -> None:
        self.duck.quack()

    def fly(self) -> None:
        if self.rand.randint(0, 1) == 0:
            self.duck.fly()


class TurkeyAdapter(Duck):
    def __init__(self, turkey: Turkey) -> None:
        self.turkey: Turkey = turkey

    def quack(self) -> None:
        self.turkey.gobble()

    def fly(self) -> None:
        for i in range(0, 5):
            self.turkey.fly()


class DroneAdapter(Duck):
    def __init__(self, drone: Drone) -> None:
        self.drone: Drone = drone

    def quack(self) -> None:
        self.drone.beep()

    def fly(self) -> None:
        self.drone.spin_rotors()
        self.drone.take_off()


class DuckTestDrive:
    def __init__(self) -> None:
        duck: Duck = MallardDuck()

        turkey: Turkey = WildTurkey()
        turkey_adapter: Duck = TurkeyAdapter(turkey)

        print("The Turkey says...")
        turkey.gobble()
        turkey.fly()

        print("\nThe Duck says...")
        self.test_duck(duck)

        print("\nThe TurkeyAdapter says...")
        self.test_duck(turkey_adapter)

    def test_duck(self, duck: Duck) -> None:
        duck.quack()
        duck.fly()


class TurkeyTestDrive:
    def __init__(self) -> None:
        duck: MallardDuck = MallardDuck()
        duck_adapter: Turkey = DuckAdapter(duck)

        for i in range(10):
            print("The DuckAdapter says...")
            duck_adapter.gobble()
            duck_adapter.fly()


if __name__ == '__main__':
    TurkeyTestDrive()
    DuckTestDrive()
