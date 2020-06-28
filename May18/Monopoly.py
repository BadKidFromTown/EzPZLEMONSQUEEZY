# Track a users bank balance
# A way of spending money
#Ask if they have enough
# A way of depositing money
#A way of returning the balance
# A way to calculate interest
# A way to keep a transaction history
#Create an account dictionary. 

Accounts = [{'First_Name' : 'George', 'Last_name': 'Li', 'ID': 12345, 'Code': 123445, 'Deposit': int(), 'TransHistory': [] }]

def Create_Account(First_Name, Last_Name, ID, Code, Deposit):
    Accounts.append({'First_Name' : First_Name, 'Last_name': Last_Name, 'ID': ID, 'Code': Code, 'Deposit': Deposit, 'TransHistory': [] })
    print('The code is how you access your account. Please put them in safe hands.')
    return Accounts

def Account_Balance(ID):
    Number_Of_Accounts = len(Accounts)
    ID_Verified = False
    x = 0
    Verified_Account = None
    Verified_Account_Balance = int()
    while x < Number_Of_Accounts and not(ID_Verified == True):
        if Accounts[x]['ID'] == ID:
            ID_Verified = True
            Verified_Account = Accounts[x]
        else:
            ID_Verified = False
        x = x + 1
    if ID_Verified == True:
        Verified_Account_Balance = Verified_Account['Deposit']
        return Verified_Account_Balance
    else:
        return None

def Account_Verification(ID, Code):
    Verify = False
    for x in range(len(Accounts)):
        if ID == Accounts[x]['ID']:
            Verified = True
        break

    if Verified == True:
        if Code == Accounts[x]['Code']:
            Verify = True
        else: 
            Verify = False
    return Verify
def Deposit(ID,Code, Money_To_Deposit):
    Number_Of_Accounts = len(Accounts)
    if Account_Verification(ID, Code) == True:
        x = 0
        while x < Number_Of_Accounts:
            if Accounts[x]['ID'] == ID:
                Serial_Number = x
            x = x + 1
        Accounts[Serial_Number]['Deposit'] = Accounts[Serial_Number]['Deposit'] + Money_To_Deposit
        Accounts[Serial_Number]['TransHistory'].append("Depositing " + str(Money_To_Deposit) + " Dollars")
        return Accounts[Serial_Number]['Deposit']
    else:
        return None

        

def Spending(ID,Code, Money_To_Spend):
    Number_Of_Accounts = len(Accounts)
    if Account_Verification(ID, Code) == True:
        x = 0
        while x < Number_Of_Accounts:
            if Accounts[x]['ID'] == ID:
                Serial_Number = x
            x = x + 1
        Accounts[Serial_Number]['Deposit'] = Accounts[Serial_Number]['Deposit'] - Money_To_Spend
        Accounts[Serial_Number]['TransHistory'].append("Spending " + str(Money_To_Spend) + " Dollars")
        return  Accounts[Serial_Number]['Deposit']
    else:
        return None

def Interest_Calculator(ID):
    Number_Of_Accounts = len(Accounts)
    ID_Verified = False
    x = 0
    No_Balance_To_Search = "There is no such account. Getta out and sign up one or I will call the police"
    while x < Number_Of_Accounts and not(ID_Verified == True):
        if Accounts[x]['ID'] == ID:
            ID_Verified = True
        else:
            ID_Verified = False
        x = x + 1
    if ID_Verified == True:
        Net_Interest = Account_Balance(ID) * 0.01
        Annual_Interest = Account_Balance(ID) + Account_Balance(ID) * 0.01
        return "Annual Interest in our bank is 1 %. Which means after 1 year you get a new balance of " + str(Annual_Interest) + " Dollars, with " + str(Net_Interest) + " as your annual interest."
    else: 
        return No_Balance_To_Search


def Track_History(ID, Code):
    Trans_History = []
    if (Account_Verification(ID, Code)) == True:
        x = 0
        while x < len(Accounts):
            if Accounts[x]['ID'] == ID:
                Trans_History = Accounts[x]['TransHistory']
            x = x + 1
        return Trans_History
    else: 
        return None

      
def main():
    Zombie = Account_Balance(12345)
    print(Zombie)
    Plant = Deposit(12345, 123445, 100)
    print(Plant)
    Haha = Spending(12345, 123445, 100)
    print(Haha)
    Interest = Interest_Calculator(12345)
    print(Interest)
    Something = Track_History(12345,123445)
    print(Something)


if __name__ == "__main__":
    main()