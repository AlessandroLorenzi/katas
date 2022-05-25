from rpg_game.character import Character


class CannotHitSelfError(Exception):
    pass


class CombatSystem:
    @classmethod
    def attack(cls, character: Character, target: Character, points: int):
        if character is target:
            raise CannotHitSelfError

        if  target.get_level() - character.get_level() >= 5 :
            target.damage(points * 0.5)
            return
        
        if character.get_level() - target.get_level()  >= 5:
            target.damage(points * 1.5)
            return
            
        target.damage(points)

    @classmethod
    def heal(cls, character: Character, points: int):
        character.heal(points)
