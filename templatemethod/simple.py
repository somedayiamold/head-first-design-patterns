class Coffee:
    def prepare_recipe(self) -> None:
        self.boil_water()
        self.brew_coffee_grinds()
        self.pour_in_cup()
        self.add_sugar_and_milk()

    def boil_water(self) -> None:
        print('Boiling water')

    def brew_coffee_grinds(self) -> None:
        print('Dripping Coffee through filter')

    def pour_in_cup(self) -> None:
        print('Pouring into cup')

    def add_sugar_and_milk(self) -> None:
        print('Adding Sugar and Milk')


class Tea:
    def prepare_recipe(self) -> None:
        self.boil_water()
        self.steep_tea_bag()
        self.pour_in_cup()
        self.add_lemon()

    def boil_water(self) -> None:
        print('Boiling water')

    def steep_tea_bag(self) -> None:
        print('Steeping the tea')

    def pour_in_cup(self) -> None:
        print('Pouring into cup')

    def add_lemon(self) -> None:
        print('Adding Lemon')


if __name__ == '__main__':
    tea: Tea = Tea()
    coffee: Coffee = Coffee()
    print('Making tea...')
    tea.prepare_recipe()
    print('Making coffee...')
    coffee.prepare_recipe()
