from Stack_And_Queue import Stack
import random


def Stack_Inversion():
    a_cool_variable = Stack()
    for x in range(10):
        a_cool_variable.append(random.randint(1,10))
#    Array = Stack().Stack
    print(a_cool_variable.Stack)
    Stack_OverFlow = Stack()
    i = len(a_cool_variable.Stack)-1
    while i >= 0:
        Stack_OverFlow.append(a_cool_variable.consult())
        a_cool_variable.remove()
        i = i - 1
    return Stack_OverFlow




def main():

    The_Beautiful_Girl = Stack_Inversion().Stack
    print(The_Beautiful_Girl)


    
main()
    



# Inversion using Queue
# Inversion using Recursion without any extra structure. Print everything and not in a list.