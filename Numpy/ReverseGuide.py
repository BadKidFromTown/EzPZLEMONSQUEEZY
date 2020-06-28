import random
def Reverse_Method(Range):
    The_Array = []
    y = 0
    while y < Range:
        The_Array.append(random.randint(1,100))
        y = y + 1
    print(len(The_Array))
    print(The_Array)
    Reverse_Length = len(The_Array) / 2
    print(Reverse_Length)
    x = 0
    while x < Reverse_Length:
        The_Array[x], The_Array[len(The_Array)-1-x] = The_Array[len(The_Array)-1-x], The_Array[x]
        x = x + 1
    print(The_Array)


def main():
    Reverse_Method(11)

if __name__ == "__main__":
    main()

