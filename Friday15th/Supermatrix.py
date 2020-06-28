import random
def SuperMatrix(Side):
    Big_Array = []
    for x in range(Side):
        Small_Array = []
        for x in range(Side):
            Small_Array.append(random.randint(0,100))
        print(Small_Array)
#nested loops
        
        Big_Array.append(Small_Array)
    print("Array of Arrays = " + str(Big_Array))
    # for x in range(Side):
    #     Small_Array.append(random.randint(0,100))
    print(Big_Array[0][2])
    return(Big_Array)

def main():
    print("Now please. Enter your favorite number")
    StorageFactor = SuperMatrix(int(input()))
    print(StorageFactor)

if __name__ == "__main__":
    main()
