

my_list = [99,4,2,5,-3]
my_tuple = (99,4,2,5,-3)
my_str = "sequoia"
print(my_list[:])
# output: [99,4,2,5,-3]
print(my_tuple[1:])
# output: (4,2,5,-3)
print(my_str[:3])
# output: "seq"
print(my_tuple[2:4])
# output: (2,5)
print(my_list, my_tuple, my_str)
# output: [99,4,2,5,-3] (99,4,2,5,-3) 'sequoia' -- note the original values have not changed
print(sorted(my_str))

# stacks = 4
# # traditional
# if stacks >= 3:
#     print('Coding Dojo')
# else:
#     print('You are not Coding Dojo!')
# # ternary
# print('Coding Dojo' if stacks >= 3 else 'You are not Coding Dojo!')

# def reverse_list(x):
#     if len(x) % 2 == 0:
#         halflen = len(x) / 2
#     else:
#         halflen = (len(x) - 1) / 2
#     halfleni = int(halflen)
#     for i in range (halfleni):
#         x[i], x[len(x) - i - 1] = x[len(x) - i - 1], x[i]
#     return x

# print(reverse_list([37,2,1,-9,5]))



# dojo = {
#    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
#    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
# }

# def printInfo(dojo):
#     for key in dojo:
#         print(len(dojo[key]), key.upper())
#         for i in range (len(dojo[key])):
#             print(dojo[key][i])
#         print("\n")

# printInfo(dojo)

# students = [
#          {'first_name':  'Michael', 'last_name' : 'Jordan'},
#          {'first_name' : 'John', 'last_name' : 'Rosales'},
#          {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#          {'first_name' : 'KB', 'last_name' : 'Tonel'}
#     ]

# def iterateDictionary2(mykey, mylist):
#     for x in mylist:
#         print(x[mykey])
# iterateDictionary2("last_name", students)

# def iterateDictionary(some_list):
#     for x in some_list:
#         print("first_name -", x["first_name"],", last_name -",x["last_name"]  )
# iterateDictionary(students) 

# mydict={}
# def ultimate_analysis(x):
#     #the syntax is: mydict[key] = "value"
#     mydict["sumTotal"] = sum(x)
#     mydict["average"] = average(x)
#     mydict["minimum"] = minimum(x)
#     mydict["maximum"] = maximum(x)
#     mydict["length"] = len(x)
#     return mydict

# def maximum(x):
#     if len(x) == 0:
#         return False
#     mymax = x[0]
#     for i in range (len(x)):
#         if x[i] > mymax:
#             mymax = x[i]
#     return mymax

# def minimum(x):
#     if len(x) == 0:
#         return False
#     mymin = x[0]
#     for i in range (len(x)):
#         if x[i] < mymin:
#             mymin = x[i]
#     return mymin

# def average(x):
#     return sum(x) / len(x)

# print(ultimate_analysis([37,2,1,-9]))

# mydict={}
# def ultimate_analysis(x):
#     #the syntax is: mydict[key] = "value"
#     mydict["sumTotal"] = sum(x)
#     mydict["average"] = average(x)
#     mydict["minimum"] = minimum(x)
#     mydict["maximum"] = maximum(x)
#     mydict["length"] = len(x)
#     return mydict


# def maximum(x):
#     if len(x) == 0:
#         return False
#     mymax = x[0]
#     for i in range (len(x)):
#         if x[i] > mymax:
#             mymax = x[i]
#     return mymax
# # print(maximum([37,2,1,-9]))
# # print(maximum([]))

# def minimum(x):
#     if len(x) == 0:
#         return False
#     mymin = x[0]
#     for i in range (len(x)):
#         if x[i] < mymin:
#             mymin = x[i]
#     return mymin

# # print(minimum([37,2,1,-9]))
# # print(minimum([]))

# # def length(x):
# #     return len(x)
# # print(length([37,2,1,-9,6,7,8,9,1,2,3,4,5]))
# # print(length([]))

# def average(x):
#     return sum(x) / len(x)
# # print(average([1,2,3,4]))
# print(ultimate_analysis([37,2,1,-9]))
# # def sum_total(x):
# #     p = 0
# #     for i in range (len(x)):
# #         p += x[i]
# #     return p
# # print(sum_total([1,2,3,4]))
# # print(sum_total([-1,1]))

# # def count_positives(x):
# #     p = 0
# #     for i in range (len(x)):
# #         if x[i] > 0:
# #             p += 1
# #     x[len(x) - 1] = p
# #     return x
# # print(count_positives([-1,1,1,1]))
# # print(count_positives([1,6,0,-2,-7,-2]))

# # def biggie_size(x):
# #     for i in range(len(x)):
# #         if x[i] > 0:
# #             x[i] = "big"
# #     return x
# # print(biggie_size([-1, 3, 5, -5]))


# # def length_and_value(l,v):
# #     for i in range(0, l, 1):
# #         new_list.append(v)
# #     return new_list
# # new_list = []
# # print(length_and_value(6,2))
# # new_list = []
# # print(length_and_value(4,7))

# # new_list = []
# # def values_greater_than_second(l):
# #     if len(l) < 3:
# #         return False
# #     print(l[2])
# #     for i in range(0, len(l), 1):
# #         if l[i] >= l[2]:
# #             new_list.append(l[i])
# #     return new_list

# # values_greater_than_second([5,2])
# # print(new_list)
# # print(values_greater_than_second([5,2]))

# # my_list=[1,2,3,4,5]
# # def first_plus_length(l):
# #     return (l[0] + len(l))
# # print(first_plus_length(my_list))

# # my_list = ["abc", 123, "xyz"]
# # print("Index   Data")
# # for i in range(0, len(my_list)):
# #     print(i, "     ", my_list[i])
# # # output: 0 abc, 1 123, 2 xyz


# # def print_and_return(p,r):
# #     print(p)
# #     return r
# # print(print_and_return(1,2))


# # countlist = []
# # def countdown(num):
# #     for i in range (num, -1, -1):
# #         countlist.append(i)
# #     return countlist
# # print(countdown(5))

# # def add(a,b):	# function name: 'add', parameters: a and b
# #     x = a + b	# process
# #     return x	# return value: x
# # my_list = ["abc", 123, "xyz"]
# # print("Index   Data")
# # for i in range(0, len(my_list)):
# #     print(i, "     ", my_list[i])
# # # output: 0 abc, 1 123, 2 xyz