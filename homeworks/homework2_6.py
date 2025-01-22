class Car:
    def action(self):
        print("класс машины")

class BMW(Car):
    def action(self):
        print("БМВ наследовалась")
        super().action()

class Mercedec(Car):
    def action(self):
        print("Мерседес наследовался")
        super().action()

class Audi(BMW, Mercedec):
    def action(self):
        print("Ауди наследовалась")
        super().action()


audi = Audi()
audi.action()
