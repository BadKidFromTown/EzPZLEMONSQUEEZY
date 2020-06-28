import random


def Random_Generated_Digits(Range, Lower_Limit, Upper_Limit):
    Array_Of_random_digits = []
    for x in range(Range):
        Array_Of_random_digits.append(random.randint(Lower_Limit, Upper_Limit))
    return Array_Of_random_digits


def Find_The_Smallest(Array):
    Value = Array[0]
    for x in range(len(Array)):
        if Value > Array[x]:
            Value = Array[x]
    return Value




def main():
    Random = Random_Generated_Digits(5,5,10)
    print(Random)
    Smallest = Find_The_Smallest(Random)
    print(Smallest)



if __name__ == "__main__":
    main()
        
