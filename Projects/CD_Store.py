class CD_Store:
    def __init__(self, Storage = 1):
        self.SKU = ''
        self.price = ''
        self.Storage = Storage
        self.Name = ''
        self.Customer_List = []
    
    def Sell(self,Customer, Amount):
        self.SKU = "Item has been sold"
        self.price = None
        self.Customer_List.append(Customer)
        self.Storage = self.Storage - Amount

    def Change_SKU(self, SKU):
        self.SKU = SKU
    

    def Display_SKU(self):
        return self.SKU
    def Buy_In(self,Amount):
        self.Storage = self.Storage + Amount
    
    def Total_Storage(self):
        return self.Storage
    
    def Get_Price(self):
        return self.price
    
    def Change_Price(self,price):
        self.price = price
        return 'You have successfully changed Price. the Price of ' + self.Name + ' has been changed to ' + str(self.price)
    def Check_Who_Brought_It(self):
        return self.Customer_List
    def Check_Summary(self):
        return 'SKU = ' + self.SKU + 'price = ' + self.price + 'Storage = ' + self.Storage




def main():
    CD1 = CD_Store()
    CD1.Buy_In(100)
    CD1.Total_Storage()
    CD1.Change_SKU(100)
    CD1.Change_Price(100)

main()

