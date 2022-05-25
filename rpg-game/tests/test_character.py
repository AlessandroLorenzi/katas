from rpg_game import Character

class TestCharter:
    def test_charter(self):
        dante = Character(1)
        
        assert True == dante.is_alive()


    def test_damage(self):
        dante = Character(1)
        
        dante.damage(100)
        assert True == dante.is_alive()

        dante.heal(100)
        assert True == dante.is_alive()


        dante.damage(1000)
        assert False == dante.is_alive()
