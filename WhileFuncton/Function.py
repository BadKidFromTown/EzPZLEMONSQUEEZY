def Array_Identifier(Number, Array):
    i = 0
    StorageFactor = -1
    while i < len(Array):
        if Array[i] == Number:
            StorageFactor = i
            break
        i = i+1
    print("The position of the number inside Array is at " + str(StorageFactor))

Array_Identifier(10,[7,8,7,10,10])