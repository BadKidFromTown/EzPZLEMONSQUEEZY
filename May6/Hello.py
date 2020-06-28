for x in range(0,101):
    Fizz = x % 3
    Butt = x % 5
    if(Fizz == 0):
        print("Fizz")
    if(Butt == 0):
        print("Butt")
    if(Fizz == 0 and Butt == 0):
        print("Fizz Butt")
    else:
        print(x)