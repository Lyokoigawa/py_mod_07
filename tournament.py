from ex0.creature import CreatureFactory
from ex2.strategies import BattleStrategy
from ex2 import (
                 DefensiveStrategy,
                 AggressiveStrategy)
import ex0
import ex1
import ex2

Opponent = tuple[CreatureFactory, BattleStrategy]


def strategy_type(strategy: BattleStrategy) -> str:
    if isinstance(strategy, AggressiveStrategy):
        return "Aggressive"
    elif isinstance(strategy, DefensiveStrategy):
        return "Defensive"
    return "Normal"


def battle(participants: list[Opponent]) -> None:
    i1 = 0
    i2 = 1
    if len(participants) < 1:
        print("The tournament needs more participants!")
    else:
        for _ in range(len(participants)):
            while i2 < len(participants):
                creature1 = [participants[i1][0].create_base(),
                             participants[i1][1]]
                creature2 = [participants[i2][0].create_base(),
                             participants[i2][1]]
                print("* Battle *")
                print(creature1[0].describe())
                print("  vs.")
                print(creature2[0].describe())
                print("  now fight!")
                creature1[1].act(creature1[0])
                if creature1[1].is_valid(creature1[0]):
                    creature2[1].act(creature2[0])
                print()
                i2 += 1
            i1 += 1
            i2 = i1 + 1


if __name__ == "__main__":
    i = 0
    salandle = (ex0.FlameFactory, ex2.DefensiveStrategy())
    psyren = (ex0.AquaFactory, ex2.NormalStrategy())
    sprootly = (ex1.HealFactory, ex2.DefensiveStrategy())
    echocho = (ex1.TransformFactory, ex2.AggressiveStrategy())
    matches = [[psyren, sprootly],
               [salandle, sprootly],
               [psyren, sprootly, echocho]]
    print("Tournament 0 (basic)")
    print(f"  [ (Psyren+{strategy_type(psyren[1])}), "
          f"(Sprootly+{strategy_type(sprootly[1])}) ]")
    print("*** Tournament ***")
    print(f"{len(matches[0])} opponents involved")
    print()
    battle(matches[0])
    print("Tournament 1 (error)")
    print(f"  [ (Salandle+{strategy_type(salandle[1])}), "
          f"(Sprootly+{strategy_type(sprootly[1])}) ]")
    print("*** Tournament ***")
    print(f"{len(matches[1])} opponents involved")
    print()
    battle(matches[1])
    print("Tournament 2 (multiple)")
    print(f"  [ (Psyren+{strategy_type(psyren[1])}), "
          f"(Sprootly+{strategy_type(sprootly[1])}), "
          f"(Echocho+{strategy_type(echocho[1])}) ]")
    print("*** Tournament ***")
    print(f"{len(matches[2])} opponents involved")
    print()
    battle(matches[2])
