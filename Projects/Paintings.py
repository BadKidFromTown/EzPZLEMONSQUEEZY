from Book_Section import Book_Section
class Paintings(Book_Section):
    def __init__(self,Storage=1):
        super().__init__(Storage)
        self.Year = None
    def Set_Year(self, Year):
        self.Year = Year
    def Get_Year(self):
        return self.Year
def main():
    A_Painting = Paintings()
    A_Painting.Set_Year(1990)
    A_Painting.Change_SKU(100)

    print(A_Painting.Display_SKU())
main()