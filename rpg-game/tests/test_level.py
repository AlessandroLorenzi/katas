from rpg_game.level import Level


class TestLevel:
    def test_level(self):
        my_level = Level(1)
        assert 1 == int(my_level)

        my_level.increase()
        assert 2 == int(my_level)

        my_level.increase(2)
        assert 4 == int(my_level)
