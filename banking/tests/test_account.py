from banking import Account
from freezegun import freeze_time
import sys
from io import StringIO
from contextlib import redirect_stdout


class TestAccount:
    def test_account(self):
        a = Account()
        a.deposit(500, "10/01/2022")
        a.withdraw(400, "13/01/2022")

        f = StringIO()
        with redirect_stdout(f):
            a.print_statement()
        sys.stdout = sys.__stdout__

        assert 100 == a.get_balance()

        assert (
            """date || credit || debit || balance
13/01/2022 || || 400 || 100
10/01/2022 || 500 || || 500
"""
            == f.getvalue()
        )

    @freeze_time("2022-04-08")
    def test_account_transactions_today(self):
        a = Account()
        a.deposit(500)
        a.withdraw(400)

        f = StringIO()
        with redirect_stdout(f):
            a.print_statement()
        sys.stdout = sys.__stdout__

        assert 100 == a.get_balance()
        assert (
            """date || credit || debit || balance
08/04/2022 || || 400 || 100
08/04/2022 || 500 || || 500
"""
            == f.getvalue()
        )
