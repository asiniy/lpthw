from sys import exit

def gold_room():
    print("This room is full of gold")

    gold_amount = num(input("> "))

    if gold_amount == False:
        dead("Please learn to type the numbers")

    if gold_amount < 50:
        print("You're not greedy, you win")
        exit(0)
    else:
        dead("You're greedy bastard!")

def num(arg):
    try:
        return int(arg)
    except ValueError:
        return false

def dead(reason):
    print(reason, "Good job")
    exit(0)

gold_room()
