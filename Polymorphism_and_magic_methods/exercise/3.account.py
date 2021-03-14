from abc import ABC


class Account(ABC):
    def __init__(self, owner, amount=0):
        self.owner = owner
        self.amount = amount

    def add_transaction(self, amount):
        pass

    def balance(self):
        pass

    def validate_transaction(self, account: Account, amount_to_add):
        pass

