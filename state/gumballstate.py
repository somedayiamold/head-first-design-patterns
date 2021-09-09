from abc import ABCMeta, abstractmethod


class State(metaclass=ABCMeta):
    @abstractmethod
    def insert_quarter(self) -> None:
        raise NotImplementedError('`insert_quarter` method not implemented')

    @abstractmethod
    def eject_quarter(self) -> None:
        raise NotImplementedError('`eject_quarter` method not implemented')

    @abstractmethod
    def turn_crank(self) -> None:
        raise NotImplementedError('`turn_crank` method not implemented')

    @abstractmethod
    def dispense(self) -> None:
        raise NotImplementedError('`dispense` method not implemented')

    @abstractmethod
    def refill(self) -> None:
        raise NotImplementedError('`refill` method not implemented')


class HasQuarterState(State):
    def __init__(self, gumball_machine) -> None:
        self.gumball_machine = gumball_machine

    def insert_quarter(self) -> None:
        print("You can't insert another quarter")

    def eject_quarter(self) -> None:
        print("Quarter returned")
        self.gumball_machine.set_state(self.gumball_machine.get_no_quarter_state())

    def turn_crank(self) -> None:
        print("You turned...")
        self.gumball_machine.set_state(self.gumball_machine.get_sold_state())

    def dispense(self) -> None:
        print("No gumball dispensed")

    def refill(self) -> None:
        pass

    def __str__(self) -> str:
        return "waiting for turn of crank"


class NoQuarterState(State):
    def __init__(self, gumball_machine) -> None:
        self.gumball_machine = gumball_machine

    def insert_quarter(self) -> None:
        print("You inserted a quarter")
        self.gumball_machine.set_state(self.gumball_machine.get_has_quarter_state())

    def eject_quarter(self) -> None:
        print("You haven't inserted a quarter")

    def turn_crank(self) -> None:
        print("You turned, but there's no quarter")

    def dispense(self) -> None:
        print("You need to pay first")

    def refill(self) -> None:
        pass

    def __str__(self) -> str:
        return "waiting for quarter"


class SoldOutState(State):
    def __init__(self, gumball_machine) -> None:
        self.gumball_machine = gumball_machine

    def insert_quarter(self) -> None:
        print("You can't insert a quarter, the machine is sold out")

    def eject_quarter(self) -> None:
        print("You can't eject, you haven't inserted a quarter yet")

    def turn_crank(self) -> None:
        print("You turned, but there are no gumballs")

    def dispense(self) -> None:
        print("No gumball dispensed")

    def refill(self) -> None:
        self.gumball_machine.set_state(self.gumball_machine.get_no_quarter_state())

    def __str__(self) -> str:
        return "sold out"


class SoldState(State):
    def __init__(self, gumball_machine) -> None:
        self.gumball_machine = gumball_machine

    def insert_quarter(self) -> None:
        print("Please wait, we're already giving you a gumball")

    def eject_quarter(self) -> None:
        print("Sorry, you already turned the crank")

    def turn_crank(self) -> None:
        print("Turning twice doesn't get you another gumball!")

    def dispense(self) -> None:
        self.gumball_machine.release_ball()
        if self.gumball_machine.get_count() > 0:
            self.gumball_machine.set_state(self.gumball_machine.get_no_quarter_state())
        else:
            print("Oops, out of gumballs!")
            self.gumball_machine.set_state(self.gumball_machine.get_soldout_state())

    def refill(self) -> None:
        pass

    def __str__(self) -> str:
        return "dispensing a gumball"


class GumballMachine:
    def __init__(self, number_gumballs: int) -> None:
        self.soldout_state = SoldOutState(self)
        self.no_quarter_state = NoQuarterState(self)
        self.has_quarter_state = HasQuarterState(self)
        self.sold_state = SoldState(self)

        self.count = number_gumballs
        if number_gumballs > 0:
            self.state: State = self.no_quarter_state
        else:
            self.state = self.soldout_state

    def insert_quarter(self) -> None:
        self.state.insert_quarter()

    def eject_quarter(self) -> None:
        self.state.eject_quarter()

    def turn_crank(self) -> None:
        self.state.turn_crank()
        self.state.dispense()

    def release_ball(self) -> None:
        print("A gumball comes rolling out the slot...")
        if self.count > 0:
            self.count -= 1

    def get_count(self) -> int:
        return self.count

    def refill(self, count: int) -> None:
        self.count += count
        print(f"The gumball machine was just refilled; its new count is: {self.count}")
        self.state.refill()

    def set_state(self, state: State) -> None:
        self.state = state

    def get_state(self) -> State:
        return self.state

    def get_soldout_state(self) -> SoldOutState:
        return self.soldout_state

    def get_no_quarter_state(self) -> NoQuarterState:
        return self.no_quarter_state

    def get_has_quarter_state(self) -> HasQuarterState:
        return self.has_quarter_state

    def get_sold_state(self) -> SoldState:
        return self.sold_state

    def __str__(self) -> str:
        result = []
        result.append("\nMighty Gumball, Inc.")
        result.append("\nPython-enabled Standing Gumball Model #2021")
        result.append(f"\nInventory: {self.count} gumball")
        if self.count != 1:
            result.append("s")
        result.append("\n")
        result.append(f"Machine is {self.state}\n")
        return "".join(result)


if __name__ == '__main__':
    gumball_machine: GumballMachine = GumballMachine(2)

    print(gumball_machine)

    gumball_machine.insert_quarter()
    gumball_machine.turn_crank()

    print(gumball_machine)

    gumball_machine.insert_quarter()
    gumball_machine.turn_crank()
    gumball_machine.insert_quarter()
    gumball_machine.turn_crank()

    gumball_machine.refill(5)
    gumball_machine.insert_quarter()
    gumball_machine.turn_crank()

    print(gumball_machine)
