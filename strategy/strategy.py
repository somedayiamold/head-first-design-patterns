from abc import ABCMeta, abstractmethod


class QuackBehavior:
    __metaclass__ = ABCMeta

    @abstractmethod
    def quack(self) -> None:
        raise NotImplementedError('quack method not implemented')


class FlyBehavior:
    __metaclass__ = ABCMeta

    @abstractmethod
    def fly(self) -> None:
        raise NotImplementedError('fly method not implemented')


class Quack(QuackBehavior):
    def quack(self) -> None:
        print('Quack')


class Squeak(QuackBehavior):
    def quack(self) -> None:
        print('Quack')


class FakeQuack(QuackBehavior):
    def quack(self) -> None:
        print('Squeak')


class MuteQuack(QuackBehavior):
    def quack(self) -> None:
        print('<< Silence >>')


class FlyNoWay(FlyBehavior):
    def fly(self) -> None:
        print("I can't fly")


class FlyRocketPowered(FlyBehavior):
    def fly(self) -> None:
        print("I'm flying with a rocket")


class FlyWithWings(FlyBehavior):
    def fly(self) -> None:
        print("I'm flying!!")


class Duck:
    __metaclass__ = ABCMeta

    def __init__(self) -> None:
        self.fly_behavior: FlyBehavior = None
        self.quack_behavior: QuackBehavior = None

    def set_fly_behavior(self, fb: FlyBehavior) -> None:
        self.fly_behavior = fb

    def set_quack_behavior(self, qb: QuackBehavior) -> None:
        self.quack_behavior = qb

    def perform_fly(self) -> None:
        self.fly_behavior.fly()

    def perform_quack(self) -> None:
        self.quack_behavior.quack()

    def swim(self):
        print('All ducks float, even decoys!')

    @abstractmethod
    def display(self) -> None:
        raise NotImplementedError('display method not implemented')


class MallardDuck(Duck):
    def __init__(self) -> None:
        self.quack_behavior = Quack()
        self.fly_behavior = FlyWithWings()

    def display(self) -> None:
        print("I'm a real Mallard duck")


class RedHeadDuck(Duck):
    def __init__(self) -> None:
        self.fly_behavior = FlyWithWings()
        self.quack_behavior = Quack()

    def display(self) -> None:
        print("I'm a real Red Headed duck")


class ModelDuck(Duck):
    def __init__(self) -> None:
        self.fly_behavior = FlyNoWay()
        self.quack_behavior = Quack()

    def display(self) -> None:
        print("I'm a model duck")


class RubberDuck(Duck):
    def __init__(self) -> None:
        self.fly_behavior = FlyNoWay()
        self.quack_behavior = Squeak()

    def display(self) -> None:
        print("I'm a rubber duckie")


class DecoyDuck(Duck):
    def __init__(self) -> None:
        self.set_fly_behavior(FlyNoWay())
        self.set_quack_behavior(MuteQuack())

    def display(self) -> None:
        print("I'm a duck Decoy")


class MiniDuckSimulator:
    def __init__(self):
        mallard: MallardDuck = MallardDuck()
        rubber_duckie: RubberDuck = RubberDuck()
        decoy: DecoyDuck = DecoyDuck()

        model: Duck = ModelDuck()

        mallard.perform_quack()
        rubber_duckie.perform_quack()
        decoy.perform_quack()

        model.perform_fly()
        model.set_fly_behavior(FlyRocketPowered())
        model.perform_fly()


class MiniDuckSimulator1:
    def __init__(self):
        mallard: Duck = MallardDuck()
        mallard.perform_quack()
        mallard.perform_fly()

        model: Duck = ModelDuck()
        model.perform_fly()
        model.set_fly_behavior(FlyRocketPowered())
        model.perform_fly()


if __name__ == '__main__':
    MiniDuckSimulator()
    MiniDuckSimulator1()
