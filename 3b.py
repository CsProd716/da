class Account:
    def __init__(self,account_name,balance,rate):
        self.account_name=account_name
        self.balance = balance
        self.rate = rate
    def interest_add(self):
        a = float(input("How much interest you want to add?"))
        self.rate+=a
    def deposit(self):
        dep = float(input("How much money you want to deposit?"))
        self.balance+=dep
    def withdraw(self):
        wit = float(input("How much money you want to withdraw?"))
        if wit > self.balance:
            print("Insufficient balance")
        else:
            if wit > 20000:
                print("A fee of 100 will be charged to withdraw more than 20000.")
                i = int(input("Do you want to continue. If Yes: Press 1"))
                if i == 1:
                    print("Please wait...")
                    self.balance = self.balance-wit-100
                else:
                    exit()
            else:
                self.balance = self.balance-wit
    def statement(self):
        print("The current balance in your account is: ",self.balance)
        print("Interest rate: ", self.rate, "%")

print("Enter the new account number,initial balance and rate of interest applied")
newacc = Account(int(input()),float(input()),float(input()))
while 1:
    print("Menu:")
    print("1. Add Balance")
    print("2. Withdraw Balance")
    print("3. Increace Interest Rate")
    print("0. EXIT")
    k = int(input("Choose from the menu"))
    if k == 0:
        print("Thank you...")
        print("Exiting...")
        exit()
    elif k == 1:
        newacc.deposit()
        q = int(input("If you want to see you current statement,press 1 , else 0"))
        if q == 1:
            newacc.statement()
        elif q == 0:
            continue
    elif k == 2:
        newacc.withdraw()
        q = int(input("If you want to see you current statement,press 1 , else 0"))
        if q == 1:
            newacc.statement()
        elif q == 0:
            continue
    elif k == 3:
        newacc.interest_add()
        q = int(input("If you want to see you current statement,press 1 , else 0"))
        if q == 1:
            newacc.statement()
        elif q == 0:
            continue
     
         
                  
            
            
