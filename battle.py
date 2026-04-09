import ex0


if __name__ == "__main__":
    print("Testing fire creature factory")
    flame_base = ex0.FlameFactory.create_base()
    flame_evol = ex0.FlameFactory.create_evolved()
    print(flame_base.describe())
    print(flame_base.attack())
    print(flame_evol.describe())
    print(flame_evol.attack())
    print()

    print("Testing water creature factory")
    aqua_base = ex0.AquaFactory.create_base()
    aqua_evol = ex0.AquaFactory.create_evolved()
    print(aqua_base.describe())
    print(aqua_base.attack())
    print(aqua_evol.describe())
    print(aqua_evol.attack())
    print()

    print("Testing battle")
    print(f"{flame_base.describe()}\n"
          "   vs.\n"
          f"{aqua_base.describe()}\n"
          "  fight!")
    print(f"{flame_base.attack()}\n{aqua_base.attack()}")
