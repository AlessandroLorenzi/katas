from .health import Health
from .level import Level

class Character:

    def __init__(self, level: int):
        self.__level = Level(level)
        self.__health = Health()

    def is_alive(self) -> bool:
        return float(self.__health) > 0

    def damage(self, points: float):
        self.__health.decrease(points)

    def heal(self, points: float):
        if not self.is_alive():
            return

        self.__health.increase(points)

    def get_level(self) -> int:
        return int(self.__level)
    
    def get_health(self) -> float:
        return float(self.__health)
