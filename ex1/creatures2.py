from .capabilities import HealCapability, TransformCapability
from ex0.creature import Creature


class Sprootly(Creature, HealCapability):
    def __init__(self) -> None:
        super().__init__("Sprootly", "Grass")

    def attack(self) -> str:
        return f"{self.name} uses Vine Whip!"

    def describe(self) -> str:
        return super().describe()

    def heal(self, target: list[Creature]) -> str:
        heal_target = "itself"
        if isinstance(target, list):
            if len(target) > 1:
                heal_target = "and others"
            elif target[0].name != self.name:
                heal_target = f"and {target[0].name}"
            else:
                heal_target = "itself"
        return f"{self.name} healed {heal_target} with soothing sprouts!"


class Honeybloom(Creature, HealCapability):
    def __init__(self) -> None:
        super().__init__("Honeybloom", "Grass/Fairy")

    def attack(self) -> str:
        return f"{self.name} uses Petal Dance!"

    def describe(self) -> str:
        return super().describe()

    def heal(self, target: list[Creature]) -> str:
        heal_target = "itself"
        if isinstance(target, list):
            if len(target) > 1:
                if self in target:
                    heal_target += " and others"
                else:
                    heal_target = "others"
            elif target[0].name != self.name:
                heal_target = f"and {target[0].name}"
            else:
                heal_target = "itself"
        return f"{self.name} healed {heal_target} with healing honey!"


class Echocho(Creature, TransformCapability):
    def __init__(self) -> None:
        super().__init__("Echocho", "Normal")
        self.mode = 0

    def attack(self) -> str:
        if self.mode == 0:
            return f"{self.name} uses Echolocate!"
        else:
            return f"{self.name} uses Mob Swarm!"

    def describe(self) -> str:
        return super().describe()

    def transform(self) -> str:
        self.mode = 1
        return f"{self.name} copied itself!"

    def revert(self):
        self.mode = 0
        return f"{self.name} reabsorbed it's copies..."


class Mirrorrim(Creature, TransformCapability):
    def __init__(self) -> None:
        super().__init__("Mirrorrim", "Normal/Dark")
        self.mode = 0

    def attack(self) -> str:
        if self.mode == 0:
            return f"{self.name} uses Self-Reflection!"
        else:
            return f"{self.name} uses Mirrored Strike!"

    def describe(self) -> str:
        return super().describe()

    def transform(self):
        self.mode = 1
        return f"{self.name} became a mirror image of it's opponent!"

    def revert(self):
        self.mode = 0
        return f"{self.name} became itself again..."
