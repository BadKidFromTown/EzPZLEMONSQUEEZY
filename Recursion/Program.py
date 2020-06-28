from Dog import Dog


def main():
    dog_1 = Dog()
    dog_2 = Dog()

    dog_1.set_name('Java')
    dog_2.set_name('C++')

    dog_1.set_breed('Golden Retriever')
    dog_2.set_breed('Golden Retriever')

    dog_1.add_trick('Play dead')
    dog_2.add_trick('Say Hi')

    print(dog_1.tricks)
    
    main()