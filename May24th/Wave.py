import random
def Random_Generated_Array(Range, Lower, Upper):
    Array=[]
    for x in range(Range):
        Array.append(random.randint(Lower, Upper))
    return Array



def Snake_man(Array, Time):
    x = 0
    while x < Time + 1:
        After_Snaking = []
        y = -1
        while y < len(Array) - 1:
            After_Snaking.append(Array[y])
            y = y + 1
        Array = After_Snaking
        x = x + 1
    return After_Snaking


def main():
    Array = Random_Generated_Array(5, -5, 10)
    print(Array)
    Snaking = Snake_man(Array, 2)
    print(Snaking)


if __name__ == "__main__":
    main()

            
            

