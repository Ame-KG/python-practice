# User Input
# input("Prompt") store it in a variable
#_______________________________________________________________________________________________________

# ARITHMETIC OPERATIONS:
#-----------------------

#Exponent:
# x ** y - raises x to the power of y

#Floor devision:
# 9 // 3.5 - divides but returns the answer rounded off to the nearest whole number

# Mod:
# 10 % 3 - outputs the remainder of te fraction

#EXAMPLE USING INPUT AND MATH - asks user for number than subtracts 5 from that number:
#num = input('Enter Number: ') 
#print(int(num) - 5)

#________________________________________________________________________________________________________

# STRING METHODS:
#---------------------
# A method is something with a dot operator - e.g .upper(), .lower()

# Upper case example
# greeting = "HELLO"
# print( greeting.upper())

# Count - counts the specified character in the word in this case counts the amount of l'S
#print(greeting.count('L'))

#________________________________________________________________________________________________________

# Conditions: 
#------------

# == - checks for equlity - note: a simgle = is for assignment
# !+ - not equels
# <= - less than or =
# >= - greater or =
# < - less than
# > - greater than

# Example - code to check if x and y are the same, if yes it will return True else it will return False
# x = 10
# y = 10
# print( x == y) - prints True

# Chained Conditionals - uses AND, OR, NOT  to chain conditionals
# x = 7
# y = 8
# z = 0

# result1 = x == y - False
# result2 = y > x - True
# result3 = z < (x + 2) - True

#result 4 = result1 or result2 - this means if the left(res1) or right(res2) are true then res4 is true, if neither are true then res4 is False

#________________________________________________________________________________________________________

# LISTS AND TUPLES:
#------------------------

# Lists use square brackets
# Order is maintained
# x = [2, True, 'Hi']

# adding to lists
# x.append('Howzit')

# extending lists with other list
# x.extend([2, 3, 4, 5])

# Removing from the list - an empty bracket removes the last element in list, thyp index to remove spec
# x.pop()

# printing specific elements - e.eg howzit
# print(x[1])

# changing an element at a specific index change 2 to who
# x[0] = 'who'
# lists are mutable meaning they can be changed

# Tuples - similar to lists but immutable
# uses round brackets

# t = (2, 3, 4, 'Nice')

# YOU CAN HAVE A TUPLE INSIDE OF A LIST AND VISCA VERCA
#______________________________________________________________________________________________________

# FOR LOOPS AND WHILE LOOPS:
#----------------------------

# while loops loop infinitly until a condition is no longer met
# a for loop iterates(loops) a specific amount of times

# example to print first 10 number - this starts at 0 so wont incclude 10
# for i in range(10):
# 	print(i)

# i could be named anything it represents the index number or position or the current number the loop is on
# whatever follows the in operator determines the amount of times it loops...
# could	be a string, list, tuple, range etc

# Self challenge - maake it only be 1 to 10
# step = 1
# for e in range(10):
# 	print(step)
# 	step += 1

# print('inter')
# Range function
# can take 3 parameters (start, stop, step) 
# if only two parameteers given (start, stop)
# if just one (stop) aand starts at 0
# improved 1 - 10
# for i in range(1, 10):
# 	print(i)
#____________________________________________________________________________________________________________

# SLICE OPERATOR:
#----------------
# Uses square brackes, colons and numbers(indexes)
# [start: stop: step] - just like range
# x = [1, 2, 3, 4, 5]
# y = ('how', 'sat', 'mars')
# s = 'ONE MAN'

# This will reverse the list or tuple or string
# x_sliced = x[::-1]
# print(x_sliced)

# This will print every other element in a string or list or tuple
# s_alternate = s[::2]
# print(s_alternate)
# Play around with it
#__________________________________________________________________________________________________________

#SETS:
#------------

# An unordered unique collection of elements
# no duplicate elements
# order is not tracked
# Is extremely fast for look ups
# Only use when position or frequency of data is not important
# NOTE: everytime you print a set the data will be in a dfferent order

# for an empty set
# x = set()

# for a set with multiple elements
# s = {4, 5, 10, 9}
# s2 = {4, 5, 8, 2, 2}
# Since there is no order you use the elements themselves not their indecies

# adding elements
# s.add(3)

# removing
# s.remove(10)

# Checking if something is in a set
# print(4 in s) # wll return true or false, in this instance will return true as 4 is infact in s

# adding sets together
# print(s.union(s2))

# difference of two sets
# print( s.difference(s2))

# etc
# print(s.imtersection(s2))
#___________________________________________________________________________________________________

# Dictionaries (hash tables, maps):
#-----------------------------------

# A key-value pair
# uses curly braces but with colons to deifferentiat from sets
# d = {'key': 'value', 'send': 'message', 'greet': 'Hi', 'number': 3}
# reference/call the key to get its value
# print(d['number']) # returns 3
# print(d['greet'])  # returns Hi

# Adding keys - in this im adding a new key-value pair
# the key beimg 'new' and the value being a list
# d['new'] = ['end', 5, 4]
# print(d)

# Dictionaries just like sets use hashes so are extremely fast
#___________________________________________________________________________________________________

# COMPREHENSIONS:
#------------------

# a one line intialisation of lists, tuples, sets and dictionaries
# EXAMPLES
# making a list for 0 to 10
# x = [i for i in range(1,11)]
# print(x)

# list of all the even numbers under 100
# s = [i for i in range(1, 101) if i%2 == 0]
# print(s)

# for tuples you cant just use the regular brackets as that will get a generator object
# specify that its a tuple
# tuple for odd numbers
# t = tuple(i for i in range(1,101) if i % 2 != 0)
# print(t)
#__________________________________________________________________________________________________

# Functions:
# use the def keyword to define the function the place parameters in parenthesies

# example a function that squares a given number
# Definer- name- (parameters):
 		# Code

# def squarer(num):
# 	sq = num * num
# 	print(sq)

# calling the function
# value = 2
# squarer(value) # will returen 2 squared

# optional parameter, equate the parameter to NONE
# Example funtion that multiplies 2 numbers but if given a thir parameter multiplies 3
# def multiplyer(a, b, c=None):
# 	if c == None:
# 		print(a*b)
# 	else:
# 		print(a*b*c)
# multiplyer(1, 2)
# multiplyer(2, 3, 2)		
#___________________________________________________________________________________________________

# STAR ARGS AND STAR KWAARGS:
#--------------------------

# Unpack operator- using the asterks and will return a list/tuples elements individualy and not as a list
# x = [10, 9, 8, 4, 3]
# as a list
# print(x)
# unpacked
# print(*x)
#____________________________________________________________________________________________________

# RAISING EXCEPTION:
#---------------------
# raise Exception('bad')

# Handling exceptions
# it will use try and except blocks and will allow code to run despite an error
# try:
# 	10/0
# except Exception as e:
# 	print(e)
#__________________________________________________________________________________________________

# LAMBDAS:
#-----------

# a one line anonymous function
# a faster way of defining functions
# Example multiplyer function in lambda
# essentially they are in a way like comprehentions for functions
# x = lambda x, y: x*y
# print(x(2, 2))
#_____________________________________________________________________________________________

# MAP & FILTER FUNCTIONS:
#---------------------------

# Two built in functions that use lambdas
x = [10, 22, 485, 38, 10, 5, 100, 5]

# A map function will map to every element in a list and then apply a funtion to each one
# a map function to add 2 to every instance in the list x
# variable = map(lambda var: code, list)
twoed = map(lambda e: e + 2, x)
print(x)
print(list(twoed))
# make sure to convert the map into a list when printing

# Filter:
#--------------------------

# will go through a list and will filter out the elements that don't return true 
# this will check if the numers are even and filter out the odd numbers
filtered =filter(lambda i:i % 2 == 0, x)
print(filtered)

#__________________________________________________________________________________________________________

# F strings:
#-------------------

# allows you too embed differrent data types into strings
v = f'hello {5+5} and {x}'
print(v)