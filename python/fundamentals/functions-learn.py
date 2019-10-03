def add(a, b):  # function name: 'add', parameters: a and b
    x = a + b  # process
    return x  # return value: x


new_val = add(3, 5)    # calling the add function, with arguments 3 and 5
# the result of the add function gets sent back to and saved into new_val, so we will see 8
print(new_val)

####


def say_hi(name):
    print("Hi, " + name)


# invoking the function 3 times, passing in one argument each time
say_hi('Michael')
say_hi('Anna')
say_hi('Eli')

###


def say_hi(name):
    return "Hi " + name


# the returned value from say_hi function gets assigned to the 'greeting' variable
greeting = say_hi("Michael")
print(greeting)  # this will output 'Hi Michael'


def add(a, b):
    x = a + b
    return x


sum1 = add(4, 6)
sum2 = add(1, 4)
sum3 = sum1 + sum2
