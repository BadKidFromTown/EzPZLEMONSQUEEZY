import numpy as np 

New_World = np.array([12,3,4,5])

print(New_World.dtype)




Zombie = np.nonzero(New_World)
print(Zombie)


Zombie2 = np.where(New_World < 5, Zombie, 1)
print(Zombie2)

NewWorld = New_World*10
print(NewWorld)





def Tower_Of_Hanoi(n,Start,End,Middle):
    if n ==1: 
        print('move 1 to ' + End + "From " + Start)
    else:
        Tower_Of_Hanoi(n-1, Start, Middle, End)
        print('Moved disk' + n + ' from' + Start + ' to' + Middle)
        Tower_Of_Hanoi(n-1, Middle, Start, End)