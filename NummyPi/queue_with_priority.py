class QueueCreator:
    def __init__(self):
        self.Queue = []
    def queue(self):
        '''
        Returns Queue.
        '''
        return self.Queue





class PriorityQueue(QueueCreator):
    def __init__(self):
        super().__init__()
        self.priority = int()
        self.__value_bundle = []
    def value_editor(self, value):
        if not(self.__value_bundle == []):
            print('Value has been created. In order to delete it, please use value delete function.')
            return -1
        else:
            self.__value_bundle.append(str(value))
            print('Value creation successful.')
            return self.__value_bundle
    def priority_editor(self, priority):
        if priority > 2 or priority < 0:
            print("three priority value is 0,1,2. smaller than 0 or greater than 2 is unacceptable.")
            return -1
        elif self.__value_bundle == []:
            print('Error: Priority is not assigned.Value has not been created.')
            return -1
        else:
            self.__value_bundle.append(priority)
            return priority
    def value_deletor(self):
        self.__value_bundle = []
        return self.__value_bundle
    def Queue_Insertion(self):
        if not(len(self.__value_bundle) == 2):
            print('value insertion unsuccessful, because priority has not been assigned.')
            return -1
        else:
            if self.__value_bundle[1] == 0:
                if  self.Queue == []:
                    self.Queue.append(self.__value_bundle)
                    self.__value_bundle = []
                    return True
                else:
                    for num in range(len(self.Queue)):
                        if self.Queue[num][1] == 0 and not(self.Queue[num+1][1] == 0):
                            self.Queue.insert(num+1, self.__value_bundle)
                            self.__value_bundle = []
                    return True            
            elif self.__value_bundle[1] == 1:
                if  self.Queue[-1][1] == 1 or self.Queue[-1][1] == 0:
                    self.Queue.append(self.__value_bundle)
                    self.__value_bundle = []
                    return True
                else:
                    for num in range(len(self.Queue)):
                        if self.Queue[num][1] == 1 and self.Queue[num+1][1] == 2:
                            self.Queue.insert((num+1), self.__value_bundle)
                            self.__value_bundle = []
                    return True
            elif self.__value_bundle[1] == 2:
                self.Queue.append(self.__value_bundle)
                self.__value_bundle = []
                return True
            




