# OOP

# First Class

# add_number
# AddNumber -

# Класс
class Hero:
    def __init__(self, name, hp=100, lvl=1):
        self.name = name
        self.hp = hp
        self.lvl = lvl
    def action(self):
        return print(f"{self.name} делает первый шаг ")

    def attack(self):
        return print(f"{self.name} базовая атака")