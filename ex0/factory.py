from .creature import CreatureFactory, Creature
from . import creatures


class FlameFactory(CreatureFactory):
    def create_base() -> Creature:
        return creatures.Salandle()

    def create_evolved() -> Creature:
        return creatures.Pydramon()


class AquaFactory(CreatureFactory):
    def create_base() -> Creature:
        return creatures.Psyren()

    def create_evolved() -> Creature:
        return creatures.Olmagus()
