from Stack_And_Queue import Stack


Zombie = Stack()
print(Zombie.is_empty())



Zombie.append("Walking_Dead")
print(Zombie)

Zombie.append("Jumping_Guy")
print(Zombie)
Zombie.append("Jumping_Guy2")

Zombie.remove()
print(Zombie)
Zombie.remove()

print(Zombie.consult())

