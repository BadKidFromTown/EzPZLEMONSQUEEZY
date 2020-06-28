for x in range(0, 5):
    print("Hello Google")
List = ["P", "Q", "W"]
for x in List:
    print(x)

List_Of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for list in List_Of_lists:
    for x in list:
        print(x)
        if x == 5:
            break
    if list == List_Of_lists[1]:
        break

        
