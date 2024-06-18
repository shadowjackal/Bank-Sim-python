
from SAccount import SAccount
from CAccount import CAccount

class Customer:
    def __init__(self, custNo: int, custNm: str, age: int, city: str, accObj: object):
        self.custNo = custNo
        self.custNm = custNm
        self.age = age
        self.city = city

        # Allow for different account types (CAccount or SAccount)
        if not isinstance(accObj, (CAccount, SAccount)) and accObj != None:
            raise TypeError("accObj must be an instance of CAccount or SAccount")
        self.accObj = accObj

    def getCustNo(self) -> int:
        return self.custNo

    def getCustNm(self) -> str:
        return self.custNm

    def getAge(self) -> int:
        return self.age

    def getCity(self) -> str:
        return self.city

    def getAccObj(self) -> object:
        return self.accObj

    def __str__(self) -> str:
        # Use the account object's __str__ method for account details
        return f"""
Customer Information:

Customer Number: {self.custNo}
Customer Name: {self.custNm}
Age: {self.age}
City: {self.city}
Account Information:
{self.accObj.__str__()}
"""

# Example usage (assuming you have CAccount and SAccount classes set)
# account1 = CAccount(123456, "Savings", 1000.00)
# customer1 = Customer(1, "John Doe", 30, "New York", account1)
# print(customer1)
