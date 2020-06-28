import random 
def Matrix_Creater(Range):
    Matrix_One = []
    for x in range(Range):
        Column_1 = []
        for x in range(Range):
            Column_1.append(random.randint(1,100))
        Matrix_One.append(Column_1)
    return Matrix_One
#########################################################
def Addition_Of_Matrixes(Matrix1, Matrix2):
    Addition = []
    y = 0
    while y < len(Matrix1):
        x = 0
        Column_2 = []
        while x < len(Matrix1):
            Column_2.append(Matrix1[y][x]+ Matrix2[y][x])
            x = x + 1
        Addition.append(Column_2)
        y = y + 1
    return Addition


def main():
    print("Enter the range")
    StorageFactor = int(input())
    Matrix_First = Matrix_Creater(StorageFactor)
    print(Matrix_First)
    Matrix_Second = Matrix_Creater(StorageFactor)
    print(Matrix_Second)
    Calling = Addition_Of_Matrixes(Matrix_First,Matrix_Second)
    print(Calling)

if __name__ == "__main__":
    main()
    #Define extra method that can print the matrix