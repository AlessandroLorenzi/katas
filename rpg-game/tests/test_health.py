from rpg_game.health import Health

class TestHealth:
    def test_health(self):
        foo_health = Health()

        assert 1000.0 == float(foo_health)


    def test_decrease_increase(self):
        foo_health = Health()

        foo_health.decrease(100)
        assert 900.0 == float(foo_health)

        foo_health.increase(10)
        assert 910.0 == float(foo_health)

    def test_cannot_increase_above_max(self):
        foo_health = Health()

        foo_health.increase(1)
        assert 1000.0 == float(foo_health)

    def test_cannot_increase_under_minimum(self):
        foo_health = Health()

        foo_health.decrease(1001)
        assert 0.0 == float(foo_health)