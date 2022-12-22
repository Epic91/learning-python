class Payslips:
    def __init__(self, name, payment, amount) -> None:
        self.name = name
        self.payment = payment
        self.amount = amount
        
    def pay(self):
        self.payment = 'yes'
        
    def status(self):
        if self.payment == 'yes':
            return self.name + ' is paid out ' + str(self.amount)
        else:
            return self.name + ' is not paid yet.'
        
nathan = Payslips('Nathan', 'no', 1000)
roger = Payslips('Roger', 'no', 13000)

print(nathan.status(), '\n', roger.status())

nathan.pay()
print('After payment')
print(nathan.status(), '\n', roger.status())



class Car: 
    # Initializing the constructor 
    def __init__(self): 
        # Instance Variable 1 
        self.model = 'BMW' 
        # Instance Variable 2 
        self.color = 'red' 

# Creating objects of the class 
obj1 = Car() 
obj2 = Car() 

# Printing the value of instance variables 
print(obj1.model, obj1.color) 
print(obj2.model, obj2.color)