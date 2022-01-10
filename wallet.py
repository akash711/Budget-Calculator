import pandas as pd
import matplotlib.pyplot as plt

class Wallet:
    
    all_wallets = []

    def __init__(self, name: str):

        print("Wallet: '{}' created!".format(name))
        self.name = name
        self.ledger = []
        self.balance = 0
        self.categories = {}
        
        #Register for all wallets created
        Wallet.all_wallets.append(self)
    
    def deposit(self, amt: float, category:str):
        
        if amt >= 0:
            self.balance = self.balance + amt
        else: 
            raise Exception('Amount cannot be negative!')
        
        if category in self.categories.keys():
            self.categories[category] += amt
        else:
            self.categories[category] = amt 
        
        self.ledger.append('{} deposited'.format(amt))
        
        
        

    def withdraw(self, amt: float):
        """
        Withdraw method:
            -Withdraw money from account 
        """
        
        if amt >= 0:
            self.balance = self.balance - amt
        else:
            raise Exception('Amount cannot be negative!')

        if "Withdraw" in self.categories.keys():
            self.categories["Withdraw"] -= amt
        else:
            self.categories["Withdraw"] = -(amt) 

        self.ledger.append('{} withdrawn'.format(amt))

    
    
    def spend(self, amt: float, category: str, description: str):
        """
        Spend method:
            -Use money on specific category
        """

        if amt >= 0:
            self.balance = self.balance - amt
        else:
            raise Exception('Amount cannot be negative!')
        
        if category in self.categories.keys():
            self.categories[category] -= amt 
        else:
            self.categories[category] = -(amt)
        
        self.ledger.append('{} spent on {}: {}'.format(amt, category, description))



    def get_balance(self):
        print('Available Balance: {}'.format(self.balance))



    def transfer(self, amt: float, recepient: str):
        """
        Transfer money to recepient
        """
        
        if amt >= 0:
            self.balance = self.balance - amt
        else:
            raise Exception('Amount cannot be negative!')

        if "Transfer" in self.categories.keys():
            self.categories["Transfer"] -= amt 
        else:
            self.categories["Transfer"] = -(amt)

        self.ledger.append('{} transferred to {}'.format(amt, recepient))

    def receive(self, amt: float, sender: str):
        """
        Receive money from sender
        """
        
        if amt >= 0:
            self.balance = self.balance + amt
        else:
            raise Exception('Amount cannot be negative!')

        if "Receive" in self.categories.keys():
            self.categories["Receive"] += amt 
        else:
            self.categories["Receive"] = amt

        self.ledger.append('{} received from {}'.format(amt, sender))

        

    def read_from_excel(self, csv:str):
        
        data = pd.read_csv(csv)
        
        for i in range(len(data)):
            if data['Type'][i] == 'D':
                self.deposit(amt = data['Amount'][i], category=data['Category'][i])
            
            elif data['Type'][i] == 'T':
                self.transfer(amt = data['Amount'][i], recepient=data['Description'][i])
            
            elif data['Type'][i] == 'W':
                self.withdraw(amt = data['Amount'][i])
            
            elif data['Type'][i] == 'S':
                self.spend(amt = data['Amount'][i], category=data['Category'][i], description=data['Description'][i])
            
            elif data['Type'][i] == 'R':
                self.receive(amt = data['Amount'][i], sender=data['Description'][i])

            else:
                raise Exception('Invalid Transaction Type!')
            
    
    def print_ledger(self):
        
        for i in self.ledger:
            print(i)


    def plot_categories(self):
        
        inc = ([], [])
        exp = ([], [])
        for i in self.categories.keys():
            if self.categories[i] > 0:
                inc[0].append(self.categories[i])
                inc[1].append(i) 
            
            else:
                exp[0].append(abs(self.categories[i]))
                exp[1].append(i) 

        plt.subplot(1, 2, 1)
        plt.title('Income')
        plt.pie(labels = inc[1], x = inc[0])
        plt.subplot(1, 2, 2)
        plt.title('Expenditure')
        plt.pie(labels = exp[1], x = exp[0])

        plt.show()


    def __repr__(self):
        return "Wallet({})".format(self.name)

