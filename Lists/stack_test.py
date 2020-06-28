from Stack_And_Queue import Queue


Hello = Queue()

Hello.append("Good")
print(Hello)

Hello.append("Best")

Hello.append("Moderate")
print(Hello)

Hello.remove()

print(Hello)
Hello.remove()
print(Hello)


print(Hello.consult())
# Supposed to tell us the first element

print(Hello.is_empty())
#Check if it's empty