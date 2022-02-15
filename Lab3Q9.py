def getvalidvalue(msg, x, y):
    while True:
        value = int(input(msg))

        if x <= value <= y:
            return value
        else:
            print("Sorry, please enter within range")

mark = getvalidvalue("Enter mark: ", 0, 100)
