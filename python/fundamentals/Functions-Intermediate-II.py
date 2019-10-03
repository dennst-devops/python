# Dennis S
#Update Values in Dictionaries and Lists
x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
x[1][0]=15

# Change the last_name of the first student from 'Jordan' to 'Bryant'
sports_directory["basketball"][1] = "Bryant"

# In the sports_directory, change 'Messi' to 'Andres'
sports_directory["soccer"][0] = "Andres"

# Change the value 20 in z to 30
z[0]["y"]=30

#Iterate Through a List of Dictionaries
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
iterateDictionary(students) 
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
first_name - Michael, last_name - Jordan
first_name - John, last_name - Rosales
first_name - Mark, last_name - Guillen
first_name - KB, last_name - Tonel

# solution involves backspacing :)
def iterateDictionary(some_list):
    for x in some_list:
        print("first_name -", x["first_name"], "\b, last_name -",x["last_name"]  )
iterateDictionary(students) 

# number 3:
def iterateDictionary2(mykey, mylist):
    for x in mylist:
        print(x[mykey])
iterateDictionary2("first_name", students)
# and 
def iterateDictionary2(mykey, mylist):
    for x in mylist:
        print(x[mykey])
iterateDictionary2("last_name", students)

#4
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(dojo):
    for key in dojo:
        print(len(dojo[key]), key.upper())
        for i in range (len(dojo[key])):
            print(dojo[key][i])
        print("\n")