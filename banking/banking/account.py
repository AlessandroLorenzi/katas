from datetime import datetime


class Account:
    def __init__(self):
        self._transactions = []

    def deposit(self, amount: int, date: str = ""):
        self._add_transaction(amount, date)

    def withdraw(self, amount: int, date: str = ""):
        self._add_transaction(-amount, date)

    def _add_transaction(self, amount: int, date: str = ""):
        if date == "":
            date = datetime.today().strftime("%d/%m/%Y")
        self._transactions.append((amount, date))

    def get_balance(self) -> int:
        balance = 0
        for t in self._transactions:
            balance += t[0]
        return balance

    def print_statement(self) -> str:
        statement = []
        balance = 0
        for t in self._transactions:
            balance += t[0]
            if t[0] > 0:
                statement.append("{0} || {1} || || {2}".format(t[1], t[0], balance))
            else:
                statement.append("{0} || || {1} || {2}".format(t[1], -t[0], balance))
        statement.append("date || credit || debit || balance")
        statement.reverse()
        print("\n".join(statement))
