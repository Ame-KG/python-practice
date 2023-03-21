# Intermediate Notes
#____________________________________________________________________________________________________________

# CLASSES:
#-------------

# Defing a class
# class Dog:
	# Initialising the class- create a method(a method is a function in a class) - pass all its parametrs
	# self insures the function works on that particular object or in this case dog
	# the parameters will be attributes all dogs will have
	# def __init__(self, name, age, color):
	# 	self.name = name
	# 	self.age = age
	# 	self.color = color

	# Getting the attributes we passed to the object/dog
	# def get_name(self):
	# 	print(self.name)

	# def get_age(self):
	# 	print(self.age)

	# def get_color(self):
	# 	print(self.color)

# Creating dogs
# d1 = Dog('Blacky', 7, 'Black')
# d2 = Dog('Snappy', 5, 'Brown and White')


# # Getting their Attributes
# d1.get_color()
# d1.get_name()
# d1.get_age()

# Classes help us avoid rewriting code 
# as well as make it easier to attatch or pass multiple attributes to variables 
# If there is going to be something and theres multiple types of it and the all share certain attributes use a class

#_________________________________________________________________________________________________________

# INHERITANCE:
#--------------------

# When two classes are very similar
# Genera/Super/Parent class
# Contains all the common attributes and methods for each subclass
# class Pet:
# 	def __init__(self, name, age, color):
# 		self.name = name
# 		self.age = age 
# 		self.color = color

# 	def show(self):
# 		print(f'I am {self.name} and I am {self.age} with {self.color} hair')

# The subclasses/specific classes
# Contains attributes and methods unique to the subclass
# Made a subclass by passing the parent class in parenthesies
# class Dog(Pet):
# 	def speak(self):
# 		print('Woof')

# class Cat(Pet):
# 	def speak(self):
# 		print('Meow')

# since these are subclasses from the pet class, they inheret the methods from the Pet class

# Defining A dog
# Notice the dog class doesnt have the init method but still takes its arguments
# blacky = Dog('Blacky', 12, 'Black')
# charlie = Cat('Charlie', 8, 'White and Brown')
# charlie.speak()
# blacky.speak()
# blacky.show()
# charlie.show()

#_________________________________________________________________________________________________________

# CLASS ATTRIBUTES:
#--------------------

# Attributes that are specific to a class and not of an instance of the class
# When you use 'self' you are refering to the relevant instance/object of the class
# this would be without the use of self

# class Person:

	# This is a Class Atribute (because it does not use self, is not defined in a method and does not have access to an instance of the class)
	# number_of_people = 0


	# def __init__(self, name):
		# self.name = name 

		# This adds to the number of persons when ever an instance/object is created
		# Person.number_of_people+=1

		# We can now call the class method to add people instead of using the above code
		# Person.add_person()


	#-----------------
	# CLASS METHODS:
	#-----------------
	# Use the cls arguement and the @Classmethod decorator to define a method as a class method 
	# uses cls instead of self as it is not acting on the object but rather the class itself
	# This class method returns the number of people within the class
	# @classmethod
	# def numeber_of_persons(cls):
		# return cls.number_of_people

	# An example class method that adds to the number of people in the class
	# @classmethod
	# def add_person(cls):
		# cls.number_of_people +=1




# p1 = Person('Jimi')
# p2 = Person('Hendo')

# Can be called using the class name
# print(Person.number_of_people)

# Can be called using the instance/object of the class
# print(p1.number_of_people)

# Can be altered for the class but applies to all the instances
# Person.number_of_people = 1

# print(p2.number_of_people)

# Using Class attributes ensures you don't have to define a variable you want to remain constant..
# Outside of the class
# Also ensures that if you export/move/call a class defined in one file in another file...
# that the constant is exported as well

#________________________________________________________________________________________

# STATIC METHODS:
#--------------------

# Classes that organise functions/modules together
# Example would be importing math gives you access to math funcions
# The math module is really just a class of math methods
# Use it to orgonise funcionts that are related
# Use the STATICMETHOD DECORATOR(@ SIGN)

# Example custom math class/module

# class Math:
	# Static means non changing and thats because they do not have access to an instance which changes
	# They just do something(run code)
	# Dont have to pass self or cls as its basically just going to run as a regular function whenever called

	# @staticmethod
	# def add5(x):
	# 	return x + 5


	# @staticmethod
	# def add10(x):
	# 	return x + 5



	# @staticmethod
	# def add15(x):
	# 	return x + 5

# if this was a regular method you would have to reference the class or instance like this
# m = Math(instance)....

# now you can skip thos steps and just call it ass a function
# print(Math.add5(5))

#____________________________________________________________________________________________________

