import random
from abc import ABC, abstractmethod

# Родительский класс Hero
class Hero(ABC):
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power
        self.__random_int = random.randint(1, 3)

    def attack(self):
        print(f"{self.name} attacks with power {self.power}!")

    def protection(self):
        print(f"{self.name} defends!")

    def rest(self):
        self.health += 10
        print(f"{self.name} rests and recovers 10 health points. Current health: {self.health}")

    def get_random_int(self):
        return self.__random_int

    @abstractmethod
    def unique_attack(self):
        pass

    @abstractmethod
    def unique_scream(self):
        pass

    @abstractmethod
    def action(self):
        pass

#дочерний класс
class Jester(Hero):
    def unique_attack(self):
        print(f"{self.name} performs a trickster attack!")

    def unique_scream(self):
        print(f"{self.name} shouts: 'Laughter is the best weapon!'")

    def action(self):
        random_int = self.get_random_int()
        if random_int == 1:
            self.attack()
        elif random_int == 2:
            self.protection()
        elif random_int == 3:
            self.rest()
