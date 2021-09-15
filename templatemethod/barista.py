from abc import ABCMeta, abstractmethod


class CaffeineBeverage(metaclass=ABCMeta):
    def prepare_recipe(self) -> None:
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        self.add_condiments()

    def boil_water(self) -> None:
        print('Boiling water')

    def pour_in_cup(self) -> None:
        print('Pouring into cup')

    @abstractmethod
    def brew(self) -> None:
        raise NotImplementedError('`brew` method not implemented')

    @abstractmethod
    def add_condiments(self) -> None:
        raise NotImplementedError('`add_condiments` method not implemented')


class CaffeineBeverageWithHook(CaffeineBeverage):
    def prepare_recipe(self) -> None:
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        if self.customer_wants_condiments():
            self.add_condiments()

    def boil_water(self) -> None:
        print('Boiling water')

    def pour_in_cup(self) -> None:
        print('Pouring into cup')

    def customer_wants_condiments(self) -> bool:
        return True

    @abstractmethod
    def brew(self) -> None:
        raise NotImplementedError('`brew` method not implemented')

    @abstractmethod
    def add_condiments(self) -> None:
        raise NotImplementedError('`add_condiments` method not implemented')


class Coffee(CaffeineBeverage):
    def brew(self) -> None:
        print('Dripping Coffee through filter')

    def add_condiments(self) -> None:
        print('Adding Sugar and Milk')


class Tea(CaffeineBeverage):
    def brew(self) -> None:
        print('Steeping the tea')

    def add_condiments(self) -> None:
        print('Adding Lemon')


class CoffeeWithHook(CaffeineBeverageWithHook):
    def brew(self) -> None:
        print('Dripping Coffee through filter')

    def add_condiments(self) -> None:
        print('Adding Sugar and Milk')

    def customer_wants_condiments(self) -> bool:
        answer: str = self.get_user_input()
        if answer.lower().startswith('y'):
            return True
        return False

    def get_user_input(self) -> str:
        answer = input('Would you like milk and sugar with your coffee (y/n)? ')
        return answer


class TeaWithHook(CaffeineBeverageWithHook):
    def brew(self) -> None:
        print('Steeping the tea')

    def add_condiments(self) -> None:
        print('Adding Lemon')

    def customer_wants_condiments(self) -> bool:
        answer: str = self.get_user_input()
        if answer.lower().startswith('y'):
            return True
        return False

    def get_user_input(self) -> str:
        answer = input('Would you like lemon with your tea (y/n)? ')
        return answer


if __name__ == '__main__':
    tea: Tea = Tea()
    coffee: Coffee = Coffee()

    print('\nMaking tea...')
    tea.prepare_recipe()

    print('\nMaking coffee...')
    coffee.prepare_recipe()

    tea_hook: TeaWithHook = TeaWithHook()
    coffee_hook: CoffeeWithHook = CoffeeWithHook()

    print('\nMaking tea...')
    tea_hook.prepare_recipe()

    print('\nMaking coffee...')
    coffee_hook.prepare_recipe()
