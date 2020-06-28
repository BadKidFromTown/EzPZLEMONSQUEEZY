from CD_Store import CD_Store
class Book_Section(CD_Store):
    def __init__(self, Storage=1):
        super().__init__(Storage)
        self.Author = ''
    
    def Check_Who_Brought_The_Book(self,Name):
        super().Check_Who_Brought_It()
    
    def Change_Book_Price(self, Price):
        super().Change_Price(Price)

def main():

    Zombie = Book_Section()
    Zombie.Change_Book_Price(100)
    print(Zombie.Get_Price())


main()