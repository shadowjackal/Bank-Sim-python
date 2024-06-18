
class CAccount:
    bsbNo = 1246
    def __init__(self, accNo: int, accType: str, bal: float, minAmt=50.00):
        self.accNo = accNo
        self.accType = accType
        self.bal = bal
        self.minAmt = minAmt

    def getAccNo(self) -> int:
        return self.accNo

    def getAccType(self) -> str:
        return self.accType

    def getBal(self) -> float:
        return self.bal

    def getMinAmt(self) -> float:
        return self.minAmt

    def __str__(self) -> str:
        return f"Account No: {self.accNo}\nAccount Type: {self.accType}\nBalance: ${self.bal:.2f}\nMinimum Balance: ${self.minAmt:.2f}\n"

    def deposit(self, amount: float) -> None:
        isValid = True
        print(self)
        print(f"Amount being deposited : {amount:.2f}\n")
        if amount < 0:
                isValid = False
                print(f"deposit failed : Cannot deposite negative values\n")
        if amount > 0 and amount < self.minAmt:
                isValid = False
                print(f"deposit failed : Cannot deposite below minimum deposite amount\n")

        if isValid == True:
                self.bal += amount
                print(f"Deposit successful \n")

        print("===========================================\n")


\
