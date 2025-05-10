class bankaccount:
    def __init__(self, name, balance = 0, daily_limit = 20000):
        self.name = name
        self.balance = balance
        self.daily_limit = daily_limit
        self.withdrawn_today = 0

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError('Amount must be greater than zero.')
        self.balance += amount
        print(f":) Deposited amount Rs.{amount}. New balance : Rs.{self.balance}.")

    def withdraw(self,amount):
        if amount <= 0:
            raise ValueError('Amount must be greater than zero.')
        if amount > self.balance:
            raise RuntimeError('Insufficient funds.')
        if self.withdrawn_today + amount > self.daily_limit:
            raise RuntimeError('Withdraw limit exceeded for today.')
        
        self.balance -= amount
        self.withdrawn_today += amount
        print(f":) Withdrew amount Rs.{amount}. Remaining balance : Rs.{self.balance}.")

    def check_balance(self):
        print(f":) {self.name}'s balance : Rs.{self.balance}.")

acc = bankaccount('Meghnath',300000)
try:
    acc.deposit(0)             
except ValueError as e:
    print(f":( {e}")

try:
    acc.withdraw(70000)        
except RuntimeError as e:
    print(f":( {e}")

try:
    acc.withdraw(40000)        
    acc.withdraw(20000)        
except RuntimeError as e:
    print(f":( {e}")

acc.check_balance()

indrajeet = bankaccount('Indrajeet')
try:
    indrajeet.deposit(100)
    indrajeet.withdraw(99)
    indrajeet.deposit(500000)
    indrajeet.daily_limit = 200000
    indrajeet.withdraw(19999)
    indrajeet.check_balance()
except Exception as e:
    print(e)
