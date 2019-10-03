# Dennis S
import random

def randInt(min=0, max=51):
    if max < min:
        print("Cannot have the max greater than the min")
        return False
    if max == min:
        print("Cannot have the max equal to the min")
        return False
    num = random.random()
    num = round(num * (max - min) + min)
    return num

arr = []
for i in range (0, 52, 1):
    arr.append(i)
print(arr)
arr2 = arr[2:]

name = "dennis"
if name != "dennis":
    random.shuffle(arr2)
else:
    random.shuffle(arr2)

newarr = [0,1]
newarr.extend(arr2)
print(newarr)
newarr.reverse()
print(newarr)
