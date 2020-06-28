class Queue:
    def __init__(self):
        self.Queue = []
    def append(self,element):
        self.Queue.append(element)
    def remove(self):
        del self.Queue[0]
    def consult(self):
        return self.Queue[0]
    def is_empty(self):
        if self.Queue == []:
            return True
        else:
            return False



class Stack:
    def __init__(self):
        self.Stack = []
    def append(self,element):
        self.Stack.append(element)
        return self.Stack
    def remove(self):
        del self.Stack[-1]
    def consult(self):
        return self.Stack[-1]
    def is_empty(self):
        if self.Stack == []:
            return True
        else:
            return False



