

def Find_Addition(Number):
    Array = [1,2,3,4,5]
    Plausible_Vaules = []
    for x in range(len(Array)):
        First_Addition = Array[x]
        for y in range(len(Array)-1):
            if First_Addition + Array[y] == Number:
                if First_Addition not in Plausible_Vaules:
                    Plausible_Vaules.append(First_Addition)
                if Array[x] not in Plausible_Vaules:
                    Plausible_Vaules.append(Array[y])
    print(Plausible_Vaules)
    return Plausible_Vaules

def main():
    Something = Find_Addition(3)
    print(Something)
        
if __name__ == "__main__":
    main()