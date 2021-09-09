from enum import Enum


class State(Enum):
    SOLD_OUT: int = 0
    NO_QUARTER: int = 1
    HAS_QUARTER: int = 2
    SOLD: int = 3


class GumballMachine:
    def __init__(self, count: int) -> None:
        self.state = State.SOLD_OUT
        self.count: int = count
        if count > 0:
            self.state = State.NO_QUARTER

    def insert_quarter(self) -> None:
        if self.state == State.HAS_QUARTER:
            print("You can't insert another quarter")
        elif self.state == State.NO_QUARTER:
            self.state = State.HAS_QUARTER
            print("You inserted a quarter")
        elif self.state == State.SOLD_OUT:
            print("You can't insert a quarter, the machine is sold out")
        elif self.state == State.SOLD:
            print("Please wait, we're already giving you a gumball")

    def eject_quarter(self) -> None:
        if self.state == State.HAS_QUARTER:
            print("Quarter returned")
            self.state = State.NO_QUARTER
        elif self.state == State.NO_QUARTER:
            print("You haven't inserted a quarter")
        elif self.state == State.SOLD:
            print("Sorry, you already turned the crank")
        elif self.state == State.SOLD_OUT:
            print("You can't eject, you haven't inserted a quarter yet")

    def turn_crank(self) -> None:
        if self.state == State.SOLD:
            print("Turning twice doesn't get you another gumball!")
        elif self.state == State.NO_QUARTER:
            print("You turned but there's no quarter")
        elif self.state == State.SOLD_OUT:
            print("You turned, but there are no gumballs")
        elif self.state == State.HAS_QUARTER:
            print("You turned...")
            self.state = State.SOLD
            self.dispense()

    def dispense(self) -> None:
        if self.state == State.SOLD:
            print("A gumball comes rolling out the slot")
            self.count -= 1
            if self.count == 0:
                print("Oops, out of gumballs!")
                self.state = State.SOLD_OUT
            else:
                self.state = State.NO_QUARTER
        elif self.state == State.NO_QUARTER:
            print("You need to pay first")
        elif self.state == State.SOLD_OUT:
            print("No gumball dispensed")
        elif self.state == State.HAS_QUARTER:
            print("No gumball dispensed")

    def refill(self, num_gumballs: int) -> None:
        self.count = num_gumballs
        self.state = State.NO_QUARTER

    def __str__(self) -> str:
        result = []
        result.append("\nMighty Gumball, Inc.")
        result.append("\nPython-enabled Standing Gumball Model #2004\n")
        result.append(f"Inventory: {self.count} gumball")
        if self.count != 1:
            result.append("s")
        result.append("\nMachine is ")
        if self.state == State.SOLD_OUT:
            result.append("sold out")
        elif self.state == State.NO_QUARTER:
            result.append("waiting for quarter")
        elif self.state == State.HAS_QUARTER:
            result.append("waiting for turn of crank")
        elif self.state == State.SOLD:
            result.append("delivering a gumball")
        result.append("\n")
        return "".join(result)


if __name__ == '__main__':
    gumball_machine: GumballMachine = GumballMachine(5)

    print(gumball_machine)

    gumball_machine.insert_quarter()
    gumball_machine.turn_crank()

    print(gumball_machine)

    gumball_machine.insert_quarter()
    gumball_machine.eject_quarter()
    gumball_machine.turn_crank()

    print(gumball_machine)

    gumball_machine.insert_quarter()
    gumball_machine.turn_crank()
    gumball_machine.insert_quarter()
    gumball_machine.turn_crank()
    gumball_machine.eject_quarter()

    print(gumball_machine)

    gumball_machine.insert_quarter()
    gumball_machine.insert_quarter()
    gumball_machine.turn_crank()
    gumball_machine.insert_quarter()
    gumball_machine.turn_crank()
    gumball_machine.insert_quarter()
    gumball_machine.turn_crank()

    print(gumball_machine)
