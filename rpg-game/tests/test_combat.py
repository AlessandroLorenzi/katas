import pytest
from rpg_game import CombatSystem,Character

from rpg_game.combat import CannotHitSelfError


class TestCombat:
    def test_attack(self):
        dante = Character(1)
        cavalcante = Character(1)

        assert True == dante.is_alive()
        assert True == cavalcante.is_alive()

        CombatSystem.attack(dante, cavalcante, 100.0)
        assert True == cavalcante.is_alive()

        with pytest.raises(CannotHitSelfError):
            CombatSystem.attack(dante, dante, 100.0)

        CombatSystem.attack(dante, cavalcante, 900.0)
        assert False == cavalcante.is_alive()

    def test_heal(self):
        dante = Character(1)
        cavalcante = Character(1)

        CombatSystem.attack(dante, cavalcante, 100.0)
        CombatSystem.heal(cavalcante, 100.0)
        CombatSystem.attack(dante, cavalcante, 900.0)
        assert True == cavalcante.is_alive()

    def test_strong_target(self):
        dante = Character(5)
        cavalcante = Character(10)

        CombatSystem.attack(dante, cavalcante, 20.0)
        assert 990.0 == cavalcante.get_health()


    def test_weak_target(self):
        dante = Character(10)
        cavalcante = Character(5)

        CombatSystem.attack(dante, cavalcante, 20.0)
        assert 970.0 == cavalcante.get_health()
        