from banking import Account


class TestAccount:
    def test_account(self):
        a = Account()
        a.deposit(500, "10/01/2022")
        a.withdraw(400, "13/01/2022")
        assert 100 == a.get_balance()
        assert """date || credit || debit || balance
13/01/2022 || || 400 || 100
10/01/2022 || 500 || || 500""" == a.print_statement() 