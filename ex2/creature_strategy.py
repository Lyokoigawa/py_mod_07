from .strategies import BattleStrategy, BattleException
from ex0.creature import Creature
from ex1.capabilities import TransformCapability, HealCapability


class NormalStrategy(BattleStrategy):
    def act(self, creature: Creature) -> None:
        try:
            if self.is_valid(creature):
                print(creature.attack())
            else:
                raise BattleException
        except BattleException:
            print(f"Error - {creature.name} cannot "
                  "use the Normal strategy")

    def is_valid(self, creature: Creature) -> bool:
        result = False
        if isinstance(creature, Creature):
            result = True
        return result


class AggressiveStrategy(BattleStrategy):
    def act(self, creature: Creature) -> None:
        try:
            if self.is_valid(creature):
                print(creature.transform())
                print(creature.attack())
                print(creature.revert())
            else:
                raise BattleException
        except BattleException:
            print(f"Error - {creature.name} cannot "
                  "use the Aggressive strategy")

    def is_valid(self, creature: Creature) -> bool:
        result = False
        if isinstance(creature, TransformCapability):
            result = True
        return result


class DefensiveStrategy(BattleStrategy):
    def act(self, creature: Creature) -> None:
        try:
            if self.is_valid(creature):
                print(creature.attack())
                print(creature.heal([creature]))
            else:
                raise BattleException
        except BattleException:
            print(f"Error - {creature.name} cannot "
                  "use the Defensive strategy")

    def is_valid(self, creature: Creature) -> bool:
        result = False
        if isinstance(creature, HealCapability):
            result = True
        return result
