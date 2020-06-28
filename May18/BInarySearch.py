import random
def Bubble_Sort(Array):
    for x in range(len(Array)):
        for y in range(len(Array)-1):
            if Array[y] > Array[y+1]:
                Array[y],Array[y+1] = Array[y+1], Array[y]
    return Array

def Random_Generated_Array(Range, Lower_Limit, Upper_Limit):
    Array = []
    for x in range(Range):
        Array.append(random.randint(Lower_Limit,Upper_Limit))
    return Array


def Binary_Search(Element, Array):
    Does_Exist = False
    Lower = 0
    Upper = len(Array) - 1
    Search_Radius = Upper - Lower
    x = 0
    while x < (not(Does_Exist) and Lower <= Upper):
        if(Element == Array[Search_Radius / 2]):
            Does_Exist = True
        elif(Element > Array[Search_Radius / 2]):
            Lower = Search_Radius / 2
        elif(Element < Array[Search_Radius / 2]):
            Upper = Search_Radius / 2
        x = x + 1
    return Does_Exist


def main():
    x = Random_Generated_Array(10,-5,10)
    print(x)
    y = Bubble_Sort(x)
    print(y)
    Yes = Binary_Search(1, y)
    print(Yes)


if __name__ == "__main__":
    main()

