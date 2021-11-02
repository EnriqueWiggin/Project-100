class Atm(object):
    def __init__(self,CashWithdrawl,BankEnquiry,Deposit):
        self.CashWithdrawl=CashWithdrawl
        self.BankEnquiry=BankEnquiry
        self.Deposit=Deposit
         
    def deposit(self):
        print("deposited")

    def whitdrawl(self):
        print("withdrawled")
