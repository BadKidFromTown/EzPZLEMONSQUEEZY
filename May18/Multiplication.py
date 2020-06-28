import random
def Randomly_Generated_Matrix(Range):
    Random_Matrix = []
    for x in range(Range):
        Random_Array = []
        for y in range(Range):
            Random_Array.append(random.randint(1, 100))
        Random_Matrix.append(Random_Array)
    return Random_Matrix


def Multiplication(Matrix1, Matrix2):
    Results = []
    for x in range(len(Matrix1)):
        After_Multiply = []
        y = 0
        for y in range(len(Matrix2[0])):
            Value = 0
            z = 0
            for z in range(len(Matrix2)):
                Value = Value + Matrix1[x][z] * Matrix2[z][y]
            After_Multiply.append(Value)
        Results.append(After_Multiply)
    return(Results)


def main():
    Random1 = Randomly_Generated_Matrix(5)
    Random2 = Randomly_Generated_Matrix(5)
    print(Random1)
    print(Random2)
    Results = Multiplication(Random1, Random2)
    print(Results)
    

if __name__ == "__main__":
    main()

