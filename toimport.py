def getIntegerRange(prompt, min, max):
    while True:
        value = int(input(prompt))
      
        if min <= value <= max:
            return value
        
        print("Sorry, please re-enter within range")

def getFloatRange(prompt, min, max):
    while True:
        value = float(input(prompt))
      
        if min <= value <= max:
            return value
        
        print("Sorry, please re-enter within range")

def getCharSet(prompt, charSet):
    while True:
        value = input(prompt)
      
        if value[0] in charSet:
            return value[0]
        else:
            print("Sorry, please re-enter within range")

def getPositiveInteger(prompt):
    while True:
        value = int(input(prompt))
      
        if value > 0:
            return value
        
        print("Sorry, please enter positive integer only")