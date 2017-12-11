states = {
    'city': 'St. Petersburg',
    'Florida': 'FL',
}

print('-' * 10)
print(states['Florida'])

for state, abbrev in states.items():
    print("{} is abbreviates as {}".format(state, abbrev))

state = states.get('Texas')
print(state)

print(states.keys())
print(states.values())

print(states['nonexistant'])
