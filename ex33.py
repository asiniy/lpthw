i = 0
numbers = []

target_number = int(input("Type the number\n> "))

while i < target_number:
    print("At the top of {}".format(i))

    numbers.append(i)
    print("Numbers now {}".format(numbers))

    i += 1

print("the numbers")

for num in numbers:
    print(num)
