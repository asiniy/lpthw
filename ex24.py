print("Welcome aboard!")

poem = """
\tThe lovely word
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere is none
"""

print("---")
print(poem)
print("---")

five = 10 - 2 + 3 - 6
print("This should be five {}".format(five))

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

start_point = 1000
beans, jars, crates = secret_formula(start_point)

print("With a starting point of {}".format(start_point))
print("We'd have {} beans, {} jars, {} crates".format(beans, jars, crates))
