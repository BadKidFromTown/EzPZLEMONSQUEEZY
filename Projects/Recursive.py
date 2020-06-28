import string
def Find_Equivalency(Word, i):
    if Word[i] == Word[-i-1]:
        print(Word[i], Word[-i-1])
        if i+1 >= len(Word) / 2:
            return True
        return Find_Equivalency(Word, i+1)    # if I do that, will i reset to the initial input I have ? like if I tapped 0, and then it runs to i+1 which is 1
    else:                              # will it kind of stick to the same place since my input doesn't change, eventhough the function plus 1 to it?
        return False

def Find_Upper_Case(Word, x):
    if Word[x].isupper():
        return True
    else:
        if x == len(Word)-1:
            return False
        else:
            return Find_Upper_Case(Word, x+1)




def main():
    Resort = Find_Equivalency("1221", 0)
    print(Resort)
    Result = Find_Upper_Case("a",0)
    print(Result)
main()
