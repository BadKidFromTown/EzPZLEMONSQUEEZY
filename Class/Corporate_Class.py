from Bank_class import Bank
class Corporate(Bank):
    def __init__(self):
        self.ID_Of_This_Company = ''
        self.Interest_Rate = 0.02
        super().__init__(1, 1000)

    def Get_Corporate_Value(self,ID_Of_This_Company, ID, Password):
        if self.ID_Of_This_Company == ID_Of_This_Company:
            super().Get_Value(ID,Password)
    
    def Get_Corporate_ID(self):
        return self.ID_Of_This_Company
    
    def Interest_Calculator(self, ID_Of_This_Company, ID, Password):
        if self.ID_Of_This_Company == ID_Of_This_Company:
            return(super().Get_Value(ID,Password) * self.Interest_Rate)


