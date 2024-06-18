from Customer import Customer
from CAccount import CAccount
from SAccount import SAccount

class Bank:
    def main(self):
        print(f"Test, Init")
        # Initialize lists to store account and customer objects
        accounts = []
        customers = []

        # Read data from CAccount.CAccounts.txt and create CAccount.CAccount objects
        with open('CAccount.txt', 'r') as file:
            for line in file:
                data = line.strip().split(';')
                accNo, accType, bal = int(data[0]), data[1], float(data[2])
                if len(data) > 3:
                  minAmt = float(data[3])
                  account = CAccount(accNo, accType, bal, minAmt)
                else:
                  account = CAccount(accNo, accType, bal)

                accounts.append(account)

        # Read data from SAccount.SAccounts.txt and create SAccount.SAccount objects
        with open('SAccount.txt', 'r') as file:
            for line in file:
                data = line.strip().split(';')
                accNo, accType, bal = int(data[0]), data[1], float(data[2])
                if len(data) > 3 :
                        maxAmt = float(data[3]) 
                        account = SAccount(accNo, accType, bal, maxAmt) 
                else:
                        account = SAccount(accNo, accType, bal)
                accounts.append(account)

        # Read data from Customers.txt file to create Customer objects
        with open('Customers.txt', 'r') as file:
            for line in file:
                data = line.strip().split(';')
                custNo, custNm, age, city = int(data[0]), data[1], int(data[2]), data[3]
                customer = Customer(custNo, custNm, age, city, None)
                customers.append(customer)

        # Assign accounts to customers (assuming a round-robin assignment here for simplicity)
        for i, customer in enumerate(customers):
            if i < len(accounts):
                customer.accObj = accounts[i % len(accounts)]

        # Display account details before transactions
        for customer in customers:
            accObj = customer.getAccObj()
            if isinstance(accObj, CAccount):
                print(f"Checking Account details for customer {customer.getCustNm()}:")
                print(f"Account Number: {accObj.getAccNo()}")
                print(f"Balance: {accObj.getBal()}")
            elif isinstance(accObj, SAccount):
                print(f"Savings Account details for customer {customer.getCustNm()}:")
                print(f"Account Number: {accObj.getAccNo()}")
                print(f"Balance: {accObj.getBal()}")

        # Perform deposit transactions
        for customer in customers:
            accObj = customer.getAccObj()
            if isinstance(accObj, CAccount):
                # Invalid deposit (negative amount)
                try:
                    accObj.deposit(-100)
                except ValueError as e:
                    print(f"Invalid deposit: {e}")
                # Valid deposit
                accObj.deposit(500)
            elif isinstance(accObj, SAccount):
                # Invalid deposit (exceeding max amount)
                try:
                    accObj.deposit(100000)
                except ValueError as e:
                    print(f"Invalid deposit: {e}")
                # Valid deposit
                accObj.deposit(500)

        # Write receipts to BankingReceipt.txt
        with open('BankingReceipt.txt', 'w') as file:
            for customer in customers:
                accObj = customer.getAccObj()
                if accObj is not None:
                    file.write(f"Customer Name: {customer.getCustNm()}\n")
                    file.write(f"Account Number: {accObj.getAccNo()}\n")
                    file.write(f"Account Type: {accObj.getAccType()}\n")
                    file.write(f"Balance: {accObj.getBal()}\n\n")

if __name__ == "__main__":
    bank = Bank()
    bank.main()