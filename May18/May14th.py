import random as rd
def random_generator():
    Randomly_Generated_Matrix = []
    Column = rd.randint(1, 5)
    Row = rd.randint(1,5)
    Big_Loop = 0
    while Big_Loop < Column:
        Small_Loop = 0
        Temperary = []
        while Small_Loop < Row:
            Temperary.append(rd.randint(1,100))
            Small_Loop = Small_Loop + 1
        Randomly_Generated_Matrix.append(Temperary)
        Big_Loop = Big_Loop + 1
    return Randomly_Generated_Matrix

def transposor(Matrix):
    Swapped_Row = len(Matrix[0])
    Swapped_Column = len(Matrix)
    The_Temperary_Swapping_Storage_Factor = []
    Big_Loop = 0
    while Big_Loop < Swapped_Row:
        # The_Temperary_Swapping_Storage_Factor.append(Matrix[Big_Loop][Big_Loop])
        The_Temperary_Swapping_Storage_Factor_2 = []
        Small_Loop = 0
        while Small_Loop < Swapped_Column:
            The_Temperary_Swapping_Storage_Factor.append(Matrix[Big_Loop][Small_Loop])
            Small_Loop = Small_Loop + 1
        The_Temperary_Swapping_Storage_Factor.append(The_Temperary_Swapping_Storage_Factor_2)
        Big_Loop = Big_Loop + 1
    return The_Temperary_Swapping_Storage_Factor


def main():
    Random = random_generator()
    print(Random)
    Transposer = transposor(Random)
    print(Transposer)
    


if __name__ == "__main__":
    main()



        

