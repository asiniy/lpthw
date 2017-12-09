def fname(cars, people):
    if cars > people:
        print("We should take the cars")
    elif cars < people:
        print("We have to run by our legs")
    else:
        print("One man - one car")

fname(30, 30)
fname(40, 30)
fname(30, 40)
