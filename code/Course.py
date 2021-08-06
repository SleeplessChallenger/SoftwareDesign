from .Professor import Professor
from .Enroll import Enroll


class Course:
	def __init__(self, name, code, maxNum, minNum, professor):
		self.name = name
		self.code = code
		self.maxNum = maxNum
		self.minNum = minNum
		self.professors = []
		self.enrollments = []

		if isinstance(professor, Professor):
			self.professors.append(professor)
		elif isinstance(professor, list):
			for obj in professor:
				if isinstance(obj, Professor):
					self.professors.append(obj)
				else:
					raise TypeError('Invalid type.')
		else:
			raise TypeError('Invalid type.')

	def addProfessor(self, professor):
		if isinstance(professor, Professor):
			self.professors.append(professor)
		else:
			raise TypeError('Invalid type.')

	def addEnrollment(self, enroll):
		if isinstance(enroll, Enroll):
			if len(self.enrollments) == self.maxNum:
				raise TypeError('Course is full already:(')
			self.enrollments.append(enroll)
		else:
			raise TypeError('Invalid type.')

	def isCancelled(self):
		return len(self.enrollments) <= self.minNum
