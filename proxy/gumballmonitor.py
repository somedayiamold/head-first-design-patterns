import sys
import random
import traceback
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
        if random.randint(0, 9) == 0 and self.gumball_machine.get_count() > 1:
            self.gumball_machine.set_state(self.gumball_machine.get_winner_state())
        else:
            self.gumball_machine.set_state(self.gumball_machine.get_sold_state())

    def dispense(self) -> None:
        print("No gumball dispensed")

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

    def __str__(self) -> str:
        return "dispensing a gumball"


class WinnerState(State):
    def __init__(self, gumball_machine) -> None:
        self.gumball_machine = gumball_machine

    def insert_quarter(self) -> None:
        print("Please wait, we're already giving you a gumball")

    def eject_quarter(self) -> None:
        print("Sorry, you already turned the crank")

    def turn_crank(self) -> None:
        print("Turning again doesn't get you another gumball!")

    def dispense(self) -> None:
        print("YOU'RE A WINNER! You got two gumballs for your quarter")
        try:
            self.gumball_machine.release_ball()
            if self.gumball_machine.get_count() == 0:
                self.gumball_machine.set_state(self.gumball_machine.get_soldout_state())
            else:
                self.gumball_machine.release_ball()

                if self.gumball_machine.get_count() > 0:
                    self.gumball_machine.set_state(self.gumball_machine.get_no_quarter_state())
                else:
                    print("Oops, out of gumballs!")
                    self.gumball_machine.set_state(self.gumball_machine.get_soldout_state())
        except Exception:
            print(traceback.format_exc())

    def __str__(self) -> str:
        return "despensing two gumballs for your quarter, because YOU'RE A WINNER!"


class GumballMachine:
    def __init__(self, location: str, count: int) -> None:
        self.soldout_state: SoldOutState = SoldOutState(self)
        self.no_quarter_state: NoQuarterState = NoQuarterState(self)
        self.has_quarter_state: HasQuarterState = HasQuarterState(self)
        self.sold_state: SoldState = SoldState(self)
        self.winner_state: WinnerState = WinnerState(self)

        self.count: int = count
        if count > 0:
            self.state: State = self.no_quarter_state
        else:
            self.state = self.soldout_state
        self.location: str = location

    def insert_quarter(self) -> None:
        self.state.insert_quarter()

    def eject_quarter(self) -> None:
        self.state.eject_quarter()

    def turn_crank(self) -> None:
        self.state.turn_crank()
        self.state.dispense()

    def release_ball(self) -> None:
        print("A gumball comes rolling out the slot...")
        if self.count != 0:
            self.count -= 1

    def get_count(self) -> int:
        return self.count

    def refill(self, count: int) -> None:
        self.count = count
        self.state = self.no_quarter_state

    def set_state(self, state: State) -> None:
        self.state = state

    def get_state(self) -> State:
        return self.state

    def get_location(self) -> str:
        return self.location

    def get_soldout_state(self) -> SoldOutState:
        return self.soldout_state

    def get_no_quarter_state(self) -> NoQuarterState:
        return self.no_quarter_state

    def get_has_quarter_state(self) -> HasQuarterState:
        return self.has_quarter_state

    def get_sold_state(self) -> SoldState:
        return self.sold_state

    def get_winner_state(self) -> WinnerState:
        return self.winner_state

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


class GumballMonitor:
    def __init__(self, machine: GumballMachine) -> None:
        self.machine: GumballMachine = machine

    def report(self) -> None:
        print(f'Gumball Machine: {self.machine.get_location()}')
        print(f'Current inventory: {self.machine.get_count()} gumballs')
        print(f'Current state: {self.machine.get_state()}')


if __name__ == '__main__':
    count: int = 0

    if len(sys.argv) < 2:
        print('GumballMachine <name> <inventory>')
        sys.exit(1)

    try:
        count = int(sys.argv[2])
    except Exception:
        print(traceback.format_exc())
        sys.exit(1)

    gumball_machine: GumballMachine = GumballMachine(sys.argv[1], count)

    monitor: GumballMonitor = GumballMonitor(gumball_machine)

    print(gumball_machine)

    gumball_machine.insert_quarter()
    gumball_machine.turn_crank()
    gumball_machine.insert_quarter()
    gumball_machine.turn_crank()

    print(gumball_machine)

    gumball_machine.insert_quarter()
    gumball_machine.turn_crank()
    gumball_machine.insert_quarter()
    gumball_machine.turn_crank()

    print(gumball_machine)

    gumball_machine.insert_quarter()
    gumball_machine.turn_crank()
    gumball_machine.insert_quarter()
    gumball_machine.turn_crank()

    print(gumball_machine)

    gumball_machine.insert_quarter()
    gumball_machine.turn_crank()
    gumball_machine.insert_quarter()
    gumball_machine.turn_crank()

    print(gumball_machine)

    gumball_machine.insert_quarter()
    gumball_machine.turn_crank()
    gumball_machine.insert_quarter()
    gumball_machine.turn_crank()

    print(gumball_machine)

    monitor.report()
