#Josephus Problem: Count to number 13, delete it.
#Thought Process: Everytime make a new queue
#Based on existing array, and delete the last one. 
# Challenge: Use Recursive to do that

# def Josephus(array, i=0, previous_number=0,Queue=[],trial):
#     if array == []:
#         return previous_number
#     elif i <= (len(array)-1):
#         i = i + 1
#         Queue.append(array[i])
#         return Josephus(array,i,)
#     elif i >(len(array)-1):


def Josephus_Without_Recursion(array,trial):
    Count = trial
    previous_number = ''
    xx = 0
    #xx: responsible for looping over the array. 
    #    finds #13 on the spot and delete it.
    zz = 0
    #zz: keep track of trial. if zz equals to trial,
    #    delete the number on x and reset both to zero,
    #    with count being equal to length of the array
    #    that's left.
    for xx in range(Count+1):
        #Count: respnsible for the number of times 
        #xx has to loop over to find *trial.
        #once xx reaches count but trial requires
        #more of it, then count will be equal
        #to the times that needs to be run but 
        #haven't been ran yet.
        if len(array) ==1:
            return array
        if zz == trial:
            print('enter 2')
            previous_number = array[xx % len(array)]
            print(array[trial % len(array)])
            del array[xx % len(array)]
            xx = 0
            zz = 0
            Count = trial
        if xx > len(array)-1:
            print('enter 3',xx,len(array)-1)
            Count = Count - (len(array)-1)
            xx = 0
        zz = zz + 1


def main():
    Array = ['Bill','Michael','Lily','Emma','Danny']
    Winner = Josephus_Without_Recursion(Array,13)
    print(Winner)
         
main()

#Start with any position