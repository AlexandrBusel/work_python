class Human:
	"""docstring for Human"""
	def __init__(self, name = 'Jone', age = 25):
		
		self.name = name
		self.age = age

	def say_hello(self):
		return ('My name is {}'.format(self.name), 'me {}'.format(self.age))

class Builder(Human):

	def __init__(self, position = 'foreman'):
		self.position = position
		super().__init__()

	def say_hello(self):
		return('my name is {name}'.format(name = self.name), 'me {age}'.format(age = self.age), 'my position is {position}'.format(position = self.position))

man = Builder()
print(man.say_hello())		


class Writer(Human):
	def My_books(*args):
		books = 0
		for arg in args:
			if str(type(arg)) not in args:
				books += 1
			else:
				print('I not write books')
		print('I write', books, 'books')



	My_books('Harry Potter', 'Viking', 'Lost in space')

		



							

		