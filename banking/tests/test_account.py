from banking import Account


class TestAccount:
    def test_account(self):
        a = Account()
        a.deposit(500)
        a.withdraw(400)
        assert 100 == a.get_balance()
