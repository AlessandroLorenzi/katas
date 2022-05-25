class Level:
    def __init__(self, level: int) -> None:
        self.__level =  level

    def increase(self, levels: int = 1):
        self.__level += levels

    def __int__(self):
        return self.__level
