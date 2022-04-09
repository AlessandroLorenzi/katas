class Account:
    def __init__(self):
        self._transactions = []

    def deposit(self, amount: int, date: str = ""):
        self._add_transaction(amount, date)

    def withdraw(self, amount: int, date: str = ""):
        self._add_transaction(-amount, date)

    def _add_transaction(self, amount: int, date: str = ""):
        self._transactions.append((amount, date))

    def get_balance(self) -> int:
        balance = 0
        for t in self._transactions:
            balance += t[0]
        return balance
