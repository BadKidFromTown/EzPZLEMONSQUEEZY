#First Array
Homework = ["Math", "English", "Basketball"]
Activities = ["Reading", "Writing", "Eating"]
Day_Work = [Homework, Activities]
print("Today's schedule is " + str(Day_Work))

#The Use of cool tricks in List
Homework.append("Donuts Making")
Activities[0] = "Video Game Surfing"


#Remove and Replace
Homework[1:2] = []
print(Homework)
Homework[1:2] = ["Calculus", "Shakespeare"]
print("There are " + str(len(Homework)) + " Assignments today and " + str(len(Activities)) +" Activities to accomplish.")


###############################################################
RoomNumber = {'Zombie': 300, 'Zombies wife': 500}
del RoomNumber['Zombie']
print(RoomNumber)