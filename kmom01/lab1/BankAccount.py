"""
A BankAccount class.
"""


class BankAccount():
    """
    BankAccount handler.
    """

    def __init__(self, _owner):
        """
        Constructor.
        """
        self.balance = 113
        self._owner = _owner

    def accountInfo(self):
        """
        Returns owner and balance.
        """
        return "{owner} has {balance} kr".format(owner=self._owner, balance=self.balance)

    def getBalance(self):
        """
        Returns the balance.
        """
        return self.balance

    def depositMoney(self, amount):
        """
        Adds the amount to the balance.
        """
        self.balance += amount

    def withdrawMoney(self, amount):
        """
        Withdraws the amount of money in amount from balance.
        """
        self.balance -= amount

    def __calculateBalance(self, other):
        """
        Calculate the new balance.
        """
        result = None
        if isinstance(other, int):
            result = self.balance + other
        elif isinstance(other, BankAccount):
            result = self.balance + other.balance

        return result

    def __add__(self, other):
        """
        Adds different accounts balance together.
        """
        return self.__calculateBalance(other)

    def __iadd__(self, other):
        """
        Adds different accounts balance together.
        """
        self.balance = self.__calculateBalance(other)
        return self
