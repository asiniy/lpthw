print("You enters the dark room with 2 doors. Would you open door #1 or #2?")
choose = input("> ")

if choose == "1":
    print("You've opened the door #1")

    print("there is a giant bear. 1 - kill bear, 2 - run off")
    new_choose = input("> ")

    if new_choose == "1":
        print("Good choice. You won!")
    elif new_choose == "2":
        print("Bears are running faster than human. You've die!")
elif choose == "2":
    print("You've opened the door #2")
else:
    print("You've stay around and lose")
