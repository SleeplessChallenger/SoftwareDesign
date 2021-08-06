from .Course import Course
from .Student import Student
from datetime import datetime


class Enroll:
	def __init__(self, student, course):
		if not isinstance(student, Student):
			raise TypeError('Invalid Type.')

		if not isinstance(course, Course):
			raise TypeError('Invalid Type.')

		self.student = student
		self.course = course
		self.grade = None
		self.date = datetime.now()

	def set_grade(self, grade):
		self.grade = grade
