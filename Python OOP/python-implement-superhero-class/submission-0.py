class SuperHero:

    """
    A class to represent a superhero.

    Attributes:
        name (str): The superhero's name
        power (str): The superhero's main superpower
        health (int): The superhero's health points
    """

    def __init__(self, name: str, power: str, health: int):
        # TODO: Initialize the superhero's attributes here
        self.name = name
        self.power = power
        self.health = health


# TODO: Create Superhero instances
hero = SuperHero("Batman", "Intelligence", 100)
hero1 = SuperHero("Superman", "Strength", 150)

print(f"{hero.name}\n{hero.power}\n{hero.health}" )
print(f"{hero1.name}\n{hero1.power}\n{hero1.health}" )

# TODO: Print out the attributes of each superhero
