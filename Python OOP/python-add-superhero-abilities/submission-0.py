class SuperHero:
    """
    A class to represent a superhero.
    
    Attributes:
        name (str): The superhero's name
        power (str): The superhero's main superpower
        health (int): The superhero's health points
    """
    
    def __init__(self, name: str, power: str, health: int):
        self.name = name
        self.power = power
        self.health = health
    
    def attack(self):
        print(f"{self.name} attacks with {self.power}!")
    
    def heals(self, heal):
        self.health += heal
        print(f"{self.name} heals {heal} points. New health: {self.health}.")

ir = SuperHero("Catwoman", "Agility", 120)
hero1 = ir.attack()
hero2 = ir.heals(10)

    # TODO: Define attack method and implement it

    # TODO: Define heal method and implment it
     

# TODO: Create superhero instance


# TODO: Use the attack() and heal() method
