class Hero:
    def __init__(self, name, lvl, HP):
        self.name = name
        self.lvl = lvl
        self.HP = HP

    def introduce(self):
        print(f"Привет, меня зовут {self.name}, мой lvl {self.lvl}, мое HP {self.HP}")

    def is_adult(self):
        return self.lvl >= 10

    def __str__(self):
        return f"Имя: {self.name}, lvl: {self.lvl}, HP: {self.HP}"

hero1 = Hero("Змейка", 5, 100)
hero1.introduce()

hero2 = Hero("Леон", 10, 200)
hero2.introduce()

hero3 = Hero("Красный Шарик", 7, 150)
hero3.introduce()

print(f"{hero1.name} is adult: {hero1.is_adult()}")
print(f"{hero2.name} is adult: {hero2.is_adult()}")
print(f"{hero3.name} is adult: {hero3.is_adult()}")

print(hero1)
print(hero2)
print(hero3)
