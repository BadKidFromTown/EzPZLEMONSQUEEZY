import random



def RandomDigitGenerator(Number1,Number2,Range):
    Array = []
    for x in range(Range):
        Array.append(random.randint(Number1,Number2))
    print(Array)
def main():
    RandomDigitGenerator(5,15,5)

if __name__ == "__main__":
    main()