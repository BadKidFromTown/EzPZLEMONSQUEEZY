def Advanced_Josephus(Array,Place):
    Array_After_Arrangement = []
    #Idea is to read the starting point, regroup list based on that then execute josephus.
    #Value is the times required to loop and eliminate. 
    for x in range(len(Array)):
        if Array[x] == Place:
            Decisive_Factor = 0
            y = x
            while Decisive_Factor < 2:               
                if y == len(Array):
                    y = 0
                if Array[y] == Array[x]:
                    Decisive_Factor = Decisive_Factor + 1
                if Decisive_Factor == 2:
                    return Array_After_Arrangement
                Array_After_Arrangement.append(Array[y])
                y = y + 1


def After_Arrangement(Array,Value , Trial=13):
    After_Arrangements = Advanced_Josephus(Array,Value)
    while len(After_Arrangements) != 1:
        del After_Arrangements[len(Array) % Trial]
        print(After_Arrangements)
    return After_Arrangements


print(After_Arrangement(['Zombie','Zombie1','Zombie2'],'Zombie2'))




