#This is application: Bookshelf. 
Input = input()
def Book_Shelf (Input):
    Book_List = {}
    Option_To_Create = ""
    if(Input in Book_List):
        print("The book is stored inside your bookshelf. The name of the author is:" + Book_List[Input])
    else:
        print("The book you listed is not found. But we can store it for you. Would you like it to be put into your bookshelf? if you want to store the value, type Y. if Not, type N.")
       # yes or no
        Option_To_Create = input()
    if(Option_To_Create == "N"):
        print("Thank you for visiting your bookshelf. Hope to see you again soon!")
        
    

