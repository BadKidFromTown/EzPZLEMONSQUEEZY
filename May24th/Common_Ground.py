import random

def Random_Generated_Array(Range, Lower, Upper):
    Array=[]
    for x in range(Range):
        Array.append(random.randint(Lower, Upper))
    return Array


def Comparison(Array_One, Array_Two):
    Common_Ground = []
    # for x in range(len(Array_One)):
    #     Value = Array_One[x]
    #     for y in range(len(Array_Two)):
    #         if Value == Array_Two[y]:
    #             Common_Ground.append(Array_Two[y])
    x = 0
    while x < len(Array_One):
        Value = Array_One[x]
        y = 0

        while y < len(Array_Two):
            if Value == Array_Two[y]:
                Common_Ground.append(Array_Two[y])
            y = y + 1
        x = x + 1
    return Common_Ground

def Remove_Guy(Array):
    x = 0
    while x < len(Array):
        y = x
        while y + 1 < len(Array):
            if Array[x] == Array[y + 1]:
                del Array[y + 1]
                y = y - 1
            y = y + 1
        x = x + 1

    return Array    




    
    





def main():
    Number1 = Random_Generated_Array(10,1,10)
    Number2 = Random_Generated_Array(10,1,10)
    print(Number1, Number2)
    Gmail = Comparison(Number1, Number2)
    print(Gmail)
    Email = Remove_Guy(Gmail)
    print(Email)

    
if __name__ == "__main__":
    main()


