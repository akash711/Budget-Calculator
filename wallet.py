class Wallet:
    
    def __init__(self, name: str):
        print("Wallet: '{}' created!".format(name))
        self.name = name
        self.ledger = []
        self.balance = 0
    
    def deposit(self, amt: float):
        if amt >= 0:
            self.balance = self.balance + amt
        else: 
            raise Exception('Amount cannot be negative!')

    def withdraw(self, amt: float):
        if amt >= 0:
            self.balance = self.balance - amt
        else: 
            raise Exception('Amount cannot be negative!')


    def spend(self, amt: float, description: str):
        pass

    
    def get_balance(self):
        pass


    def check_funds(self):
        pass