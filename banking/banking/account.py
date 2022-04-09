class Account:
    def __init__(self):
        self._balance = 0

    def deposit(self, amount: int):
        self._balance += amount

    def withdraw(self, amount: int):
        self._balance -= amount

    def get_balance(self) -> int:
        return self._balance
