class Dog:
    def __init__(self):
        self.name = ''
        self.breed = ''
        self.tricks = []
    def set_name(self, name):
        self.name = name
    
    def set_breed(self, breed):
        self.breed = breed
    
    def add_trick(self, trick):
        self.tricks.append(trick)
    