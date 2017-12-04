from sys import argv

filename = argv[1]

txt = open(filename)

print("Here's your file text: {}".format(filename))
print(txt.read())
txt.close()
