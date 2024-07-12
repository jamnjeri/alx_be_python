class BankAccount:
  def __init__(self,account_balance, initial_balance=0):
    self.account_balance = account_balance
    self.initial_balance = 0
    
  def deposit(self, amount):
    self.account_balance += amount
    # print(f"Deposited: ${amount:.1f}")
    
  def withdraw(self, amount):
    if self.account_balance >= amount:
      self.account_balance -= amount
      return True
    #   print(f"Withdrew: ${amount}")
    else:
    #   print("Insufficient funds.")
      return False
    self.account_balance -= amount
    
  def display_balance(self):
    print(f"Current Balance: ${self.account_balance:.2f}")