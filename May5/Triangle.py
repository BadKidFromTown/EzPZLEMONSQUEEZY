
print("Please type in three lengths, respecively.")
print("Length A:")
Length1 = int(input())
print("Length B:")
Length2 = int(input())
print("Length C:")
Length3 = int(input())
if(Length1 + Length2 < Length3 or Length1 + Length3 < Length2 or Length2 + Length3 < Length1):
    print("They cannot form a triangle.")
else:
        if(Length1 + Length2 == Length3 or Length1 + Length3 == Length2 or Length2 + Length3 == Length1):
            print("The triangle is called a 'Degenerate'.")
        else:
            if(Length1 + Length2 > Length3 and Length1 + Length3 > Length2 and Length2 + Length3 > Length1):
                print("Looks like you got yourself a triangle.")
