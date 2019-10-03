#Dennis S
#1
def a():
    return 5
print(a())
# predicted 5
# actual 5

#2
def a():
    return 5
print(a()+a())
# predicted 10
# actual 10


#3
def a():
    return 5
    return 10
print(a())
# predicted 5
# actual 5


#4
def a():
    return 5
    print(10)
print(a())
# predicted 5
# actual 5


#5
def a():
    print(5)
x = a()
print(x)
# predicted 5
# actual 5, None
# looks like the x value is shown as none scince a() has no return


#6
def a(b,c):
    print(b+c)
print(a(1,2) + a(2,3))
# predicted 3 + 5
# actual TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'
# Looks like an usupported overload for the plus sign (NoneType)


#7
def a(b,c):
    return str(b)+str(c)
print(a(2,5))
# predicted 25
# actual 25


#8
def a():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(a())
# predicted 100, 10
# actual 100, 10

#9
def a(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(a(2,3))
print(a(5,3))
print(a(2,3) + a(5,3))
# predicted 7, 14, 21
# actual 7, 14, 21


#10
def a(b,c):
    return b+c
    return 10
print(a(3,5))
# predicted 8
# actual 8


#11
b = 500
print(b)
def a():
    b = 300
    print(b)
print(b)
a()
print(b)
# predicted 500, 500, 300, 300
# actual 500, 500, 300, 300
# ha, lucky guess on my part that b would retain its value outside of the function


#12
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
a()
print(b)
# predicted 500, 500, 300, 300
# actual 500, 500, 300, 500
# hmmm, did b lose scope leaving the function?


#13
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
b=a()
print(b)
# predicted 500, 500, 300, 500
# actual 500, 500, 300, 300
# normally I'd be on top of this but #12 has me off my game

#14
def a():
    print(1)
    b()
    print(2)
def b():
    print(3)
a()
# predicted 1, 3, 2
# actual 1, 3, 2


#15
def a():
    print(1)
    x = b()
    print(x)
    return 10
def b():
    print(3)
    return 5
y = a()
print(y)
# predicted 1, 3, 5, 10
# actual 1, 3, 5, 10
