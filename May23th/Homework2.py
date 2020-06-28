import random


def Random_Generated_Digits(Range, Lower_Limit, Upper_Limit):
    Array_Of_random_digits = []
    for x in range(Range):
        Array_Of_random_digits.append(random.randint(Lower_Limit, Upper_Limit))
    return Array_Of_random_digits

def Search_Sorting(Array):
    for x in range(0, len(Array)-1):
        Temprorary = x
        for y in range(x,len(Array)):
            if Array[Temprorary] > Array[y]:
                Temprorary = y
        Array[x], Array[Temprorary] = Array[Temprorary], Array[x]
    return Array

def main():
    SOmething = Random_Generated_Digits(5,10, 20)
    print(SOmething)
    SomeCoolStuff = Search_Sorting(SOmething)
    print(SomeCoolStuff)

if __name__ == "__main__":
    main()


                


            