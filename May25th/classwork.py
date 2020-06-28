import random
def Random_Generated_Array(Range, Lower, Upper):
    Array=[]
    for x in range(Range):
        Array.append(random.randint(Lower, Upper))
    return Array
def Get_Rid_Of_Max_And_Min(Array):
    Max = Array[0]
    Min = Array[0]
    x = 0
    while x < len(Array):
        if Max < Array[x]:
            Max = Array[x]
        if Min > Array[x]:
            Min = Array[x]
        x = x + 1
    x = 0
    while x < len(Array):
        if Max == Array[x]:
            del Array[x]
        if Min == Array[x]:
            del Array[x]
        x = x + 1
    return Array
def Average(Array):
    Sum_Of_Goodies = 0
    for x in range(len(Array)):
        Sum_Of_Goodies = Sum_Of_Goodies + Array[x]
    Average_Without_M_and_M = Sum_Of_Goodies/ len(Array)
    return Average_Without_M_and_M

def main():
    Something = Random_Generated_Array(10,1,10)
    print(Something)
    After_Getting_Rid = Get_Rid_Of_Max_And_Min(Something)
    print(After_Getting_Rid)
    Hello = Average(After_Getting_Rid)
    print(Hello)

if __name__ == "__main__":
    main()