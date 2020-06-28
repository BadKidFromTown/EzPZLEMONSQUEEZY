#i has to be initialized. i is 0 by default.
def Stack_Inversion(Stack,i=0,Inverted_Stack=[]):
    if i == (len(Stack)):
        print("Inversion Complete! Origional Stack is:" + str(Stack))
        return Inverted_Stack
    else:
        Inverted_Stack.append(Stack[-(i+1)])
        return Stack_Inversion(Stack,i+1,Inverted_Stack)
        
def main():
    Zombie = Stack_Inversion([1,2,3,4,5])
    print(Zombie)



main()