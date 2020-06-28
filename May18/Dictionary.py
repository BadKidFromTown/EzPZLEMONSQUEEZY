import random
import string




#Book_List = [{'Name' : 'Once Upon a hollywood', 'Author': 'Leonardo Decaprio', 'Time Of Release': 2019, 'ID': Id_Generator() }, {'Name' : 'It', 'Author': 'Stephen King', 'Time Of Release': 1986, 'ID': Id_Generator()}, {'Name' : '11/26/13', 'Author': 'Stephen King', 'Time Of Release': 2011, 'ID': Id_Generator()}, {'Name' : 'A beautiful day in the neighborhood', 'Author': 'Mister Rogers', 'Time Of Release': 1968, 'ID': Id_Generator()}]
Book_List = []

def Id_Generator(size = 6, charts = string.ascii_uppercase + string.digits):
    return ''.join(random.choice(charts) for x in range(size))




# def Add_Book(Book_Name, Author, Time_Of_Release):
#     # if Book_Name == Book_List.itervalues():
#     #     print("The book you have selcted is inside your book shelf.")
#         Book_List.append({})
#         Book_List[-1]['Name'] = Book_Name
#         Book_List[-1]['Author'] = Author
#         Book_List[-1]['Time Of Release'] = Time_Of_Release
#         print("The book has been added. The id number of which is" + Book_List[-1]['ID'])



# def Book_Shelf(Help):
#     if Help == True:
#         Action = input("Please print the number of your intended action to the right:\n 1. Add a book \n 2. Delete a book \n 3. Search book")
#         if int(Action) == 1:
#             Name_Of_The_Book = input("")



def Add_Book(Name, Author, Year):
    Book = {'Name': Name, 'Author': Author, 'Year': Year, 'ID': Id_Generator()}
    Book_List.append(Book)
    print("The book: " + Name + " has been added.")
    return Book


# def Bubble_Sorting(List):
#     Range = len(List)
#     for x in len(Range):
#         for y in len(Range)-1:
#             if List[y] > List[y+1]:
#                 List[y],List[y+1] = List[y+1],List[y]
#     return List
##################################################################################################################
def Bubble_Sorting(Array):
    Range = len(Array)
    for x in range(Range):
        y = 0
        for y in range(Range - 1):
            if Array[y] > Array[y+1]:
                Array[y], Array[y+1] = Array[y + 1], Array[y]
    return Array

def By_Year(List):
    Temprorary_variable = []
    for x in range(len(List)):
        Temprorary_variable_2 = List[x]['Year']
        Temprorary_variable.append(Temprorary_variable_2)
    return(Temprorary_variable)

##################################################################################################################
##################################################################################################################
########################## Put dictionaries in a choronological order
def Bubble_Sorting_Dictionaries(Array):
    Range = len(Array)
    for x in range(Range):
        y = 0
        for y in range(Range - 1):
            if Array[y]['Year'] > Array[y+1]['Year']:
                Array[y], Array[y+1] = Array[y + 1], Array[y]
    return Array
##################################################################################################################
##################################################################################################################

def Find_Book_By_Author(Array, Author):
    Range = len(Array)
    Temprorary_Variable = []
    for x in range(Range):
        if Array[x]['Author'] == Author:
            Temprorary_Variable.append(Array[x])
    return Temprorary_Variable





#####HW: Figure out how to put dictionaries in order not just years.

#https://stackoverflow.com/questions/44053440/how-to-sort-dictionaries-in-python-using-bubble-sort    -------> The answer (check after class)



####Create a function to find books by an author. Return a stack of books.
# function takes a string. INside find a new list. Can be anything. Iterate all other lists. If it matches it, append it. (Push) which is append
# At the end return the list. 



def main():
    StorageFactor = Add_Book("It", "Stephen King", 1986)
    Add_Book("The handsome George with the prettiest girlfriends", "Stephen Jobs", 2021)
    Add_Book("Life of Py", "Jimmy", 2014)
    print(StorageFactor)
    print(Book_List[0]['Year'])
    Something = By_Year(Book_List)
    print(Something)
    # print(StorageFactor[0]['Year'])
    # StorageFactor2 = Bubble_Sorting([1,9,2,6,5,7,4,3])
    # print(StorageFactor2)
    Another_Thing = Bubble_Sorting(Something)
    print(Another_Thing)
    ##Printing dictionaries in order with regard to year of publishing
    Google = Bubble_Sorting_Dictionaries(Book_List)
    print(Google)
    ##################################################################################################################
    DuckDuckGo = Find_Book_By_Author(Book_List, 'Jimmy')
    print(DuckDuckGo)
    ##################################################################################################################
if __name__ == "__main__":
    main()
