from .Address import Address

class Person:
	def __init__(self, first, last, dob, phone, address):
		self.first_name = first
		self.last_name = last
		self.date_of_birth = dob
		self.phone = phone
		self.addresses = []

		if isinstance(address, Address):
			self.addresses.append(address)
		elif isinstance(address, list):
			for obj in address:
				if isinstance(obj, Address):
					self.addresses.append(obj)
				else:
					raise TypeError('Invalid type.')
		else:
			raise TypeError('Invalid type.')

	def add_new_address(self, address):
		if isinstance(address, Address):
			self.addresses.append(address)
		else:
			raise TypeError('Invalid type.')

# 1 address
# Person(_, _, ..., Address())
# many addresses
# Person(_, _, ..., [Address(), Address()])