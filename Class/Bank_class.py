class Bank:
    #Global
    Is_Account_Active = True

    #Methods
    def __init__(self, Membership, Balance):
        self.Membership = Membership
        self.ID = None
        self.Password = None
        self.Account_Name = ''
        self.Initial_Balance = Balance
    def Set_ID(self, ID):
        self.ID = ID
    def Set_Password(self, Password):
        self.Password = Password
    def Set_Account_Name(self, Account_Name):
        self.Account_Name = Account_Name
    def Add_Value(self, Deposits):
        self.Initial_Balance = self.Initial_Balance + Deposits
    def Remove_Value(self, Spending):
        self.Initial_Balance = self.Initial_Balance - Spending
    def Account_Delete(self, Option):
        if Option == True:
            self.ID = None
        else:
            self.ID = self.ID
    def Get_Value(self, ID, Password):
        if self.ID == ID and self.Password == Password:
            return self.Initial_Balance
        else:
            return 'Account Does not Exist or Password has been incorrect'
    def Upgrade_Membership(self, Membership):
        self.Membership = Membership
        if self.Membership > 5:
            #5 as black diamond membership, highest possible membership
            self.Membership = 5
        return self.Membership
    def Show_ID(self):
        return self.ID
            
    
    