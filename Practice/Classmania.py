# Course and Student classes and using them together 
class Student:
	def __init__(self, name, age, grade):
		self.name = name
		self.age = age
		self.grade = grade # 0-100% 

	def get_age(self):
		return self.grade


class Course:
	def __init__(self, name, max_students):
		self.name = name
		self.max_students = max_students

		# a method to add students to the course but it is not made a paremeter and is a list
		self.students = []

	# A method that appends the student list created earlier
	def add_student(self, student):

		# IF THERE IS STILL SPACE IN THE COURSE RUN THIS CODE
		if len(self.students) < self.max_students:
			self.students.append(student)

			# IF STUDENT ADDED RETURNS TRUE
			return True
		else:
			return False

	# Getting the average grades of the students
	def get_grade_average(self):
		value = 0
		for student in self.students:
			value += student.grade
		average = value/len(self.students)
		print(str(average) + '% Is the grade average for vetinary courses')



# Creating Students
s1 = Student('Ame', 20, 55)
s2 = Student('Tasneem', 20, 60)
s3 = Student('Meshaya', 20, 85)

# Creating Courses
it = Course('Infornation Technology', 2)
pet_care = Course('Vetinary Sciences', 3)
culinary = Course('Culinary', 10)

# Adding Students to courses
it.add_student(s1)
it.add_student(s2)
pet_care.add_student(s3)
pet_care.add_student(s2)
pet_care.add_student(s1)
culinary.add_student(s2)
culinary.add_student(s3)

# Printing out the students in a course
print(it.students)

# Getting the name of the first student in IT
print(it.students[0].name)

# Getting all the students
for student in pet_care.students:
	print(student.name, student.age, student.grade)

for student in culinary.students:
	print(student.name, student.age, student.grade)

# getting the average grade in Vetinary course
pet_care.get_grade_average()


#_____________________________________________________________________________________________________
# Inheritance