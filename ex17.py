from sys import argv

script, from_file_path, to_file_path = argv

print("Copying from {:s} to {:s}".format(from_file_path, to_file_path))

from_file = open(from_file_path)
data = from_file.read()

print("The input file is {:d} bytes long".format(len(data)))

to_file = open(to_file_path, 'w')
to_file.write(data)

print("done")

from_file.close()
to_file.close()
