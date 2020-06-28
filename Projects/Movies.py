from CD_Store import CD_Store
class Movies(CD_Store):
    def __init__(self, Storage=1):
        super().__init__(Storage)
        self.Genre = ''
        self.Discount = None
    def Set_Genre(self, Genre):
        self.Genre = Genre
    def Get_Genre(self):
        return self.Genre
    def Set_Discount(self, Discount):
        self.Discount = Discount
        self.price = self.price - self.price * self.Discount


