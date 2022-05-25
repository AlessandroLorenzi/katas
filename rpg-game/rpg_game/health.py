class Health:
    __MAX_HEALTH: float =  1000.0
    __MIN_HEALTH: float = 0.0

    def __init__(self):
        self.__health = self.__MAX_HEALTH

    def decrease(self, health: float):
        self.__health -= health
        if self.__health < self.__MIN_HEALTH:
            self.__health = self.__MIN_HEALTH

    def increase(self, health: float):
        self.__health += health
        if self.__health > self.__MAX_HEALTH:
            self.__health = self.__MAX_HEALTH

    def __float__(self)->float:
        return self.__health

