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
        
        if amt >= 0:
            self.balance = self.balance - amt
        else:
            raise Exception('Amount cannot be negative!')
        
        
        print("New transaction: {}, Amount: {}".format(description, amt))
        


    def get_balance(self):
        print('Available Balance: {}'.format(self.balance))


    def send_money(self, amt, recepient):

        if amt >= 0:
            self.balance = self.balance - amt
        else:
            raise Exception('Amount cannot be negative!')
        
        print("{} sent to {}".format(amt, recepient))
        
