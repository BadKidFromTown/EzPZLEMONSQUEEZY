import random


def Random_Generated_Digits(Range, Lower_Limit, Upper_Limit):
    Array_Of_random_digits = []
    for x in range(Range):
        Array_Of_random_digits.append(random.randint(Lower_Limit, Upper_Limit))
    return Array_Of_random_digits

def Find_The_Smallest(Array):
    Array_Storage = Array
    Length = len(Array)
    for x in range(Length):
        x = 0
        if Array[x] > Array[x+1]:
            Array[x].remove()
        elif Array[x] < Array[x+1]:
            Array[x+1].remove()
        elif Array[x] == Array[x+1]:
            Array[x+1].remove()
    return Array_Storage.index(Array[0])

def main():
    Array = Random_Generated_Digits(10, -10, 10)
    print(Array)
    Smallest = Find_The_Smallest(Array)
    print(Smallest)

if __name__ == "__main__":
    main()