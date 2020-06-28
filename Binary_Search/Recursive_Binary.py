

Example_After_Modification = [1,2,3,4,5,7,8,9,10]
#Binry Search could be done easily, which has been skipped for simplicity.
#Low has to be zero when intializing. High has to be the length of the array.
#Previous Range Has To Equal To ZERO when initializing.
def Binary_Search(Array, Object, Low, High):
    Range = int((High-Low)/2)
    if Low > High:
        return False
    elif Object == Array[Range + Low]:
        return True
    elif Object > Array[Range + Low]:
        return Binary_Search(Array, Object, Range + Low + 1, High)
    elif Object < Array[Range + Low]:
        return Binary_Search(Array, Object, Low, Range + Low - 1)
    






def main():
    A_Beautiful_Unit = Binary_Search(Example_After_Modification, 6, 0, len(Example_After_Modification)-1)
    print(A_Beautiful_Unit)




main()