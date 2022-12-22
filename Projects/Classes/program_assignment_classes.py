from abc import ABC, abstractmethod

class Bank(ABC):
    
    @abstractmethod
    
    def basicinfo():
        print('This is a generic bank')
        return 'Generic bank: 0'
    
    def withdraw():
        pass
    
class Swiss(Bank):
    
    def __init__(self, bal) -> None:
        super().__init__(bal)
        self.bal = 1000
        
    def basicinfo(self):
        print('This is the Swiss Bank')
        
        if self.bal > 0:
            return 'Swiss Bank: ' + str(self.bal)
    
    def withdraw(self, amount):
        
        if amount > self.bal:
            print('insufficient funds')
            return self.bal
        else:
            new_balance = self.bal - amount
            
            print('Withdrawn amount: ' + amount)
            print('New balance: ' + new_balance)
            return new_balance