# Input = int(input())


def Perfect_Dector(Input):
    Addition = 0
    x = 1
    while x < Input:
        if(Input % x == 0):
            Addition = Addition + x
        x = x + 1
    if Addition == Input:
        print("This is thus a perfect number.")
    else:
        print("This is not a perfect number.")

def main():
    print("Please enter a perfect number.")
    Input = int(input())
    Perfect_Dector(Input)

if __name__ == "__main__" :
    main()