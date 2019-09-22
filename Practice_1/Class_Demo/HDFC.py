class HDFC_FD:
    amount=6000
    def withdraw(self,wa):
        self.amount=self.amount-wa

        return self.amount
    def deposit(self,da):
        self.amount=self.amount+da
        return self.amount
manas=HDFC_FD()
print(manas.withdraw(1000))
print(manas.deposit(10000))
