# Dennis S
import random

def randInt(min=0, max=100):
    if max < min:
        print("Cannot have the max greater than the min")
        return False
    if max == min:
        print("Cannot have the max equal to the min")
        return False
    num = random.random()
    num = round(num * (max - min) + min)
    return num

print(randInt()) 		    # should print a random integer between 0 to 100
print(randInt(max=50)) 	    # should print a random integer between 0 to 50
print(randInt(min=50)) 	    # should print a random integer between 50 to 100
# should print a random integer between 50 and 500
print(randInt(min=50, max=500))
# prints Cannot have the max greater than the min & False
print(randInt(min=50, max=-500))
# prints Cannot have the max greater than the min & False
print(randInt(min=50, max=50))
