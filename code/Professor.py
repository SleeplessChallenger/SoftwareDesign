from .Person import Person
from .Course import Course


class Professor(Person):
	'''
	Professor can go into courses, then in courses
	all enrollments can be checked, hence grade of the
	particular enrollment (hence student will be affected)
	can be tweaked
	'''
	def __init__(self, first, last, dob, phone, address, salary):
		super().__init__(first, last, dob, phone, address)
		self.salary = salary
		self.courses =[]
		self.got_raise = False

	def checkRaise(self):
		if len(self.courses) >= 3 and self.got_raise is False:
			self.salary += 20000
			self.got_raise = True

	def addCourse(self, course):
		if isinstance(course, Course):
			self.courses.append(course)
		else:
			raise TypeError('Invalid type.')
