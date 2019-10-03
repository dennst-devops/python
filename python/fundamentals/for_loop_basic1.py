# Dennis S
# Basic - Print all integers from 0 to 150.
# there are a few different ways to do this:
# for x in range(0, 151, 1):
#     print(x)
# print("first loop")
# # call out that we want one past the stopping point
for x in range(0, (150 + 1), 1):
    print(x)
# print("second loop")
# for x in range(0, 151):
#     print(x)
# print("third loop")
# for x in range(151):
#     print(x)
# print("fourth loop")

# Multiples of Five - Print all the multiples of 5 from 5 to 1,000
#2 ways to accomplish this:
for x in range(5, 1001, 5):
    print(x)

# a convoluted way:
# count = 5
# while count <= 1000:
#     if count % 5 == 0:
#         print(count)
#     count += 1

# Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. 
# If divisible by 10, print "Coding Dojo".
for x in range(1, 101, 1):
    if x % 10 == 0:
        print("Coding Dojo")
    elif x % 5 == 0:
        print("Coding")
    else:
        print(x)

# Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
final = 0
# let's try to get rid of magic numbers
end = 500000
for x in range(0, (end + 1), 1):
    final += x
print(final)

# Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
start = 2018
end = 0
for x in range(start, end , -4):
    print(x)

# Flexible Counter - Set three variables: lowNum, highNum, mult. 
# Starting at lowNum and going through highNum, print only the integers 
# that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, 
# the loop should print 3, 6, 9 (on successive lines)
lowNum = 2
highNum = 55
mult = 5
for x in range(lowNum, (highNum + 1), 1):
    if x % mult == 0:
        print(x)

