from .Person import Person
from .Enroll import Enroll


class Student(Person):
	def __init__(self, first, last, dob, phone, address, international=False):
		super().__init__(first, last, dob, phone, address)
		self.international = international
		self.enrolled = []

	def add_enrollment(self, enroll):
		if isinstance(enroll, Enroll):
			self.enrolled.append(enroll)
		else:
			raise TypeError('Invalid type.')

	def isOnProbation(self):
		return False

	def isPartTime(self):
		return len(self.enrolled) <= 3