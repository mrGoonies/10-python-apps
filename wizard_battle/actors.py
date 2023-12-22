class Wizard:
    def __init__(self, name: str, level: int):
        self.name = name
        self.level = level


class Creature:
    # Initializer / Instance Attributes
    def __init__(self, name: str, level: int):
        self.name = name
        self.level = level

    def __repr__(self):
        return "Creature: {} of level {}".format(
            self.name, self.level
        )
