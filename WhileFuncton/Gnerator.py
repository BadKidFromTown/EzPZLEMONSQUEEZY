import random
# List_Of_RandomInt = []
# x = 0 
# while x < 20:
#     y = random.randint(1,100)
#     print(y)
#     List_Of_RandomInt.append(y)
#     x = x + 1
# print(List_Of_RandomInt)
# List2 = List_Of_RandomInt.reverse()
# print(List2)

List_Of_randomInt = []
def Randomization(Range):
    x = 0
    Reverse = []
    while x < 20:
        y = random.randint(1,Range)
        print(y)
        List_Of_randomInt.append(y)
        x = x + 1
    print(List_Of_randomInt)
    Reverse = List_Of_randomInt.reverse()
    print(Reverse)


#Why when we do the way as above doesn't generate a reverse array?
def Bubble_Sort(Objective_List):
    Length = len(Objective_List)
    for i in range(Length):
        for x in range(Length - 1):
            if Objective_List[x] > Objective_List[x+1]:
                Objective_List[x],Objective_List[x+1] = Objective_List[x+1], Objective_List[x]
    print(Objective_List)



def main():
    Randomization(100)
    Bubble_Sort(List_Of_randomInt)

if __name__ == "__main__":
    main()
