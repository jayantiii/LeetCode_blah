class Bank:

    def __init__(self, balance: List[int]):
        self.balance = balance
        self.n = len(balance)
        

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if account1 < 1 or account1 > self.n or account2 < 1 or account2 >self.n:
            return False
        #Transfer from 1 to 2
        if self.balance[account1-1] >= money:
            self.withdraw(account1, money)
            self.deposit(account2, money)
            return True
        return False       

    def deposit(self, account: int, money: int) -> bool:
        if account < 1 or account >self.n:
            return False
        self.balance[account-1] += money
        return True    

    def withdraw(self, account: int, money: int) -> bool:
        if account < 1 or account > self.n:
            return False
        accbal = self.balance[account-1]
        if accbal - money >=0: #then valid
            self.balance[account-1] = accbal - money
            return True
        return False

        
#Know where where to use self. and what to put in init
#beware of 0-indexed integer array but 1...n numbered accs

# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)