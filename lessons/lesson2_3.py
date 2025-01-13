#инкапсуляция

class Hero:

    def __init__(self, name, hp=100, lvl=1):
        self.__name = name
        self.__hp = hp
        self.__lvl = lvl