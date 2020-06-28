class SmartList:
    '''
    hi gio
    '''
    def __init__(self):
        '''
        hi frans
        '''
        self.smart_list = []
        self.type = (float, int)
    

    def insert(self,number):
        # if number.type != float or int:
        #     print('cannot insert variables other than float or integers!')
        # else:
        #     if self.smart_list == []:
        #         self.smart_list.append(number)
        #     for num in range(self.smart_list):
        #         if number < self.smart_list[num]:
        #             temp_01 = self.smart_list[:num]
        #             temp_02 = self.smart_list[num:]
        #             self.smart_list.clear()
        #             for zombie in temp_01:
        #                 self.smart_list.append(zombie)
        #             self.smart_list.append(num)
        #             for zombie in temp_02:
        #                 self.smart_list.append(zombie)
        if self.smart_list == []:
            self.smart_list.append(number)
        else:
            for xx in range(len(self.smart_list)):
                if number < self.smart_list[xx]:
                    self.smart_list.insert(xx-1, number)
                    break
                if number >= self.smart_list[-1]:
                    self.smart_list.append(number)
                    break
        # elif number <= self.smart_list[0]:
        #     temp = self.smart_list
    def __length_returner(self):
        return len(self.smart_list)
    def binary_search(self,number,low=0,high= __length_returner()):
        if low > high:
            return -1
        elif number == self.smart_list[(high-low)/2]:
            medium = (high - low)/2
            return medium
        elif number > self.smart_list[(high-low)/2]:
            previous_medium = medium
            medium = (high - low)/2 + 1
            return self.binary_search(number, previous_medium + medium, high)
        elif number < self.smart_list[(high - low)/2]:
            previous_medium = medium
            medium = (high-low)/2 - 1
            return self.binary_search(number, low, previous_medium - medium)


zombie1 = SmartList()
zombie1.insert(1)
print(zombie1.smart_list)
zombie1.insert(0)
print(zombie1.smart_list)
zombie1.insert(1.5)
print(zombie1.smart_list)
zombie1.insert(0.5)
print(zombie1.smart_list)



# Finish Refininig. Queue with priority: 
# THey contain objects called nodes.
# Nodes have two attributes.
# 1) information = The element we want to insert inside of our queue
# 2) Priority Field = {0,1,2}
# 0 is the highest priority/
# 1 is the next priority
# 2 the lower priority
# inside of our queue, we sitll has one front, has one back
# the problem comes when a new element needs to be inserted inside the queue
#[0,01,1,2,2]

#queue = 1
#===> FIFO
#



