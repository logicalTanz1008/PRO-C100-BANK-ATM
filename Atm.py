class Atm:
    def __init__(self, balance):
        self.balance = balance

    def BalanceEnquiry(amount):
        print("Balance in your account is: $", amount.balance)

    def CashWithdrawal(amount):
        input1 = int(input("Enter amount to withdraw"))
        if input1>amount.balance:
            print("Earn some money rather than withdrawing it")
        else:
            print("Withdrawing money....")
            newBalance = amount.balance - input1
            print("Balance left: $", newBalance)
        
account1 = Atm(1000000)

account1.BalanceEnquiry()
account1.CashWithdrawal()
