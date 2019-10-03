# 1. TASK: print "Hello World"
print("Hello World")

# # 2. print "Hello Noelle!" with the name in a variable
name = "Dennis"
print( "Hello", name)	# with a comma
print( "Hello " + name )	# with a +

# # 3. print "Hello 42!" with the number in a variable
name = 42 # 42 is my favrorite number :)
print( "Hello", name )	# with a comma
# yes, this does give an error, commenting out the line...
# but it can be fixed by declaring 42 to be a string instead of a number
name = "42"
print( "Hello " + name)	# with a +	-- this one should give us an error!

# # 4. print "I love to eat sushi and pizza." with the foods in variables
fave_food1 = "Kakugiri Yatsuhashi"
fave_food2 = "chips & dip"
print( "I love to eat {} and {}.".format(fave_food1, fave_food2) ) # with .format()
print( f"I love to eat {fave_food1} and {fave_food2}." ) # with an f string

#trying out string methods...
print(fave_food1.upper())
print(fave_food1.lower())
import datetime
print("The year is now", datetime.datetime.now().year)
print(f"The string '{fave_food1}' is exactly", len(fave_food1), "chars long.")

#printing on one line:
print("Notice how these are printed on ", end="")
print("one line even though there are 3 ", end="")
print("different print statements.")

# escaping special chars:
print("Here is a slash: \\")
print("Here is a double quote: \"")
print("Here is a single quote: \'")
print("Here is a \nnew line")