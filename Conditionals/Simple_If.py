print("########welcome to my program ############")
print("please enter the first number")
Number1 = int(input())
print("Now, please input the second number to compare")
Number2 = int(input())


if( Number1 == Number2):
    print('The numbers are equal:')
    print(str(Number1) + " = " + str(Number2))
else:
    print("The numbers are different.")
    if(Number1 > Number2):
        print(str(Number1) + " is greater than " +str(Number2))
    else:
        print(str(Number1) + " is less than " + str(Number2))

#inside the brackets: conditions or logical expressions.