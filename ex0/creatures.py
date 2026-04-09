from .creature import Creature


class Salandle(Creature):
    def __init__(self) -> None:
        return super().__init__("Salandle", "Fire")

    def attack(self) -> str:
        return f"{self.name} uses Ember!"

    def describe(self) -> str:
        return super().describe()


class Pydramon(Creature):
    def __init__(self) -> None:
        return super().__init__("Pydramon", "Fire/Dragon")

    def attack(self) -> str:
        return f"{self.name} uses Flamethrower!"

    def describe(self) -> str:
        return super().describe()


class Psyren(Creature):
    def __init__(self) -> None:
        return super().__init__("Psyren", "Water")

    def attack(self) -> str:
        return f"{self.name} uses Water Gun!"

    def describe(self) -> str:
        return super().describe()


class Olmagus(Creature):
    def __init__(self) -> None:
        return super().__init__("Olmagus", "Water/Psychic")

    def attack(self) -> str:
        return f"{self.name} uses Hydro Pump!"

    def describe(self) -> str:
        return super().describe()
