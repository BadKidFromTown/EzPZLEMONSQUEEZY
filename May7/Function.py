def Four_Variables(name1,name2,name3,name4):
    print("Hello, +" + name1 + " , " + name2 + " , " +  name3 + " , " + " , "  + name4 + " welcome to the jungle!")



Four_Variables("George", "ZOmbie", "Plant", "Sinba")

def Save_Joe_Exotic(money1,claim1,money2,claim2): 
    Sum_Of_Money = money1 + money2
    if(Sum_Of_Money >= 500):
        print("Thank you for your donation!")
        print("The money you donated to Joe Fundation is " + str(Sum_Of_Money))
    else:
        print("you don't have enough fund to donate.")
        print("Go earn some money, big boy!")
    print(" Again, thank you for your donation. Your claim:" + claim1 + " and " + claim2 + " has been recorded. We look forward to reply you with furth details about how's it going with Joe!")


Save_Joe_Exotic(100, "Good", 200, "Bad")
Save_Joe_Exotic(100, "Bad", 400,"Good")