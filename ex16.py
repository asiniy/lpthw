from sys import argv

script, filename = argv

print("We're going to erase {!r}".format(filename))
print("Click Ctrl-C to exit, Return to proceed")

input()

print("Opening the file")
target = open(filename, "w")

print("Truncating the file. Goodbye!")
# target.truncate()

print("Now I'm asking you for a three lines")
line_1 = input("line 1: ")
line_2 = input("line 2: ")
line_3 = input("line 3: ")

print("I'm going to write these 3 lines")
target.write("{}\n{}\n{}\n".format(line_1, line_2, line_3))

print("And finally, we close it.")
target.close()
