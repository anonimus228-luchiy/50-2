class Heroes:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def action(self):
        print(f"{self.name} готовится к атаке.")

    def attack(self):
        print(f"{self.name} наносит атаку!")


class Archer(Heroes):
    def __init__(self, name, hp, arrows, precision):
        super().__init__(name, hp)
        self.arrows = arrows
        self.precision = precision

    def attack(self):
        if self.arrows > 0:
            self.arrows -= 1
            if self.precision >= 50:
                print(f"{self.name} успешно попал в цель! Осталось стрел: {self.arrows}")
            else:
                print(f"{self.name} промахнулся! Осталось стрел: {self.arrows}")
        else:
            print(f"{self.name} не может атаковать, стрелы закончились.")

    def rest(self):
        self.arrows += 5
        print(f"{self.name} пополнил стрелы. Текущее количество стрел: {self.arrows}")

    def status(self):
        return f"Имя: {self.name}, Здоровье: {self.hp}, Стрелы: {self.arrows}, Точность: {self.precision}%"


archer = Archer(name="Леголас", hp=100, arrows=10, precision=75)

archer.status()
archer.attack()
archer.rest()
print(archer.status())
