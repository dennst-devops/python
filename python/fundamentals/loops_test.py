    x = 12
    if x > 50:
    	print("bigger than 50")
    else:
    	print("smaller than 50")
    # because x is not greater than 50, the second print statement is the only one that will execute
    
    x = 55
    if x > 10:
    	print("bigger than 10")
    elif x > 50:
    	print("bigger than 50")
    else:
    	print("smaller than 10")
    # even though x is greater than 10 and 50, the first true statement is the only one that will execute, so we will only see 'bigger than 10'
    
    if x < 10:
    	print("smaller than 10"copy)
    # nothing happens, because the statement is false 

for x in range(0, 10, 1):
for x in range(0, 10):	# increment of +1 is implied
for x in range(10):	# increment of +1 and start at 0 is implied

for x in range(1, 11, 2):
    print(x, end=" ")
print("\n")
# output: 0, 2, 4, 6, 8
for x in range(5, 1, -3):
    print(x)
# output: 5, 2

my_list = ["abc", 123, "xyz"]
print("Index   Data")
for i in range(0, len(my_list)):
    print(i, "     ", my_list[i])
# output: 0 abc, 1 123, 2 xyz
    
# OR 
    
for v in my_list:
    print(v)
# output: abc, 123, xyz

my_dict = { "name": "Noelle", "language": "Python" }
for k in my_dict:
    print(k)
# output: name, language

my_dict = { "name": "Noelle", "language": "Python" }
for k in my_dict:
    print(my_dict[k])
# output: Noelle, Python

# another way to iterate through the keyscopy
for key in capitals.keys():
     print(key)
#to iterate through the values
for val in capitals.values():
     print(val)
#to iterate through both keys and values
for key, val in capitals.items():
     print(key, " = ", val)

for count in range(0,5):
    print("looping - ", count)
# The above and below are the same
count = 0
while count < 5:
    print("looping - ", count)
    count += 1

y = 3
while y > 0:
    print(y)
    y = y - 1
else:
    print("Final else statement")

for val in "string":
    if val == "i":
        break
    print(val)
# output: s, t, r

for val in "string":
    if val == "i":
        continue
    print(val)
# output: s, t, r, n, g
# notice, no i in the output, but the loop continued after the i

y = 3
while y > 0:
    print(y)
    y = y - 1
    if y == 0:
        break
else:		# only executes on a clean exit from the while loop (i.e. not a break)
   print("Final else statement")
# output: 3, 2, 1

