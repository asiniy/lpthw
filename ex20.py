from sys import argv

script, input_file_path = argv

def print_all(file):
    print(file.read())

def rewind(file):
    file.seek(0)

def print_line(line_number, f):
    print(line_number, f.readline())

input_file = open(input_file_path)

print("Firstly, print the whole file")

print_all(input_file)

rewind(input_file)



input_file.close()
