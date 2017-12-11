ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait, there isn't 10 things in this list, let's fix that")

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding", next_one)
    stuff.append(next_one)
    print("There is {} items now".format(len(stuff)))

print("Let's do some things with stuff")

print(stuff)
print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(stuff)
print(' '.join(stuff))
print('#'.join(stuff[3:5]))
