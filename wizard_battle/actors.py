class Wizard:
    def __init__(self, name: str, level: int):
        self.name = name
        self.level = level

    def attack(self, creature):
        """Wizard attacks creature
        :param creature: Creature name
        :return: None
        """
        print(f"The wizard {self.name} attacks {creature}!")


class Creature:
    # Initializer / Instance Attributes
    def __init__(self, name: str, level: int):
        self.name = name
        self.level = level

    def __repr__(self):
        return "Creature: {} of level {}".format(
            self.name, self.level
        )
