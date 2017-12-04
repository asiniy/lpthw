from sys import argv

script, user_name = argv
prompt = ">"

print("Hi {}, it's a {} script".format(script, user_name))
likes = input(prompt)

print("Likes: {}".format(likes))
