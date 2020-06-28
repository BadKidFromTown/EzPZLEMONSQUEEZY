def Amicable_Number(Input,Input2) : 
    StorageValue = 0
    StorageValue2 = 0
    x = 1
    y = 1
    while x < Input:
        if Input % x == 0 :
            StorageValue = StorageValue + x
        x = x + 1
    while y < Input2:
        if Input2 % y ==0 :
            StorageValue2 = StorageValue2 + y
        y = y + 1
    if StorageValue == Input2 and StorageValue2 == Input:
        print("Two number  you just entered are Amicable numbers.")
    else:
        print("Two number you just entered are not Amicable numbers.")

def main():
    print("Please enter the two number you want to test, respectively. ")
    print("First Number:")
    Input = int(input())
    print("Second Number:")
    Input2 = int(input())
    Amicable_Number(Input,Input2)

if __name__ == "__main__" :
    main()
