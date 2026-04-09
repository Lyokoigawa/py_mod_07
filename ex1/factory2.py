from . import creatures2
from ex0.creature import CreatureFactory, Creature


class HealFactory(CreatureFactory):
    def create_base() -> Creature:
        return creatures2.Sprootly()

    def create_evolved() -> Creature:
        return creatures2.Honeybloom()


class TransformFactory(CreatureFactory):
    def create_base() -> Creature:
        return creatures2.Echocho()

    def create_evolved() -> Creature:
        return creatures2.Mirrorrim()
