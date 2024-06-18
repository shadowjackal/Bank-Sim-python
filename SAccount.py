
class SAccount:
    # Class variable holding the BSB number (same as CAccount)
    bsbNo = 1246

    def __init__(self, accNo: int, accType: str, bal: float, maxAmt=500.00):
        # Initialize account attributes
        self.accNo = accNo
        self.accType = accType
        self.bal = bal
        self.maxAmt = maxAmt

    def getAccNo(self) -> int:
        # Return account number
        return self.accNo

    def getAccType(self) -> str:
        # Return account type
        return self.accType

    def getBal(self) -> float:
        # Return current balance
        return self.bal

    def getMaxAmt(self) -> float:
        # Return maximum allowed balance
        return self.maxAmt

    def __str__(self) -> str:
        return f"Account No: {self.accNo}\nAccount Type: {self.accType}\nBalance: ${self.bal:.2f}\nMaximum Balance: ${self.maxAmt:.2f}\n"

    def deposit(self, amount: float) -> None:
        isValid = True
        # Deposit amount into the account
        print(self)	
        print(f"Amount attempting to be deposited : {amount:.2f} \n")

        if amount < 0:
                print(f"Deposit amount cannot be negative.\n")
                isValid = False
        if amount > self.maxAmt:
                print(f"Deposit Greater than the maximum deposit limit \n")
                isValid = False
	
        if isValid == True:
                self.bal += amount 
                print(f"Successful deposit \n")
	
        print("===========================================\n")


# Example usage (assuming you want to test it)
# account1 = SAccount(123456, "Savings", 1000.00)
# print(account1)

