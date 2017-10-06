class Person:
	'''Represents a person.'''
	population = 0

	def sayHello(self):
		print("Hello,my name is %s"%self.name)

	def __init__(self, name): #类似于构造函数
		'''Initializes the person's data.'''
		self.name = name
		print("(Initializing %s)"%self.name)

		Person.population += 1

	def __del__(self): #类似于析构函数
		'''I am dying.'''
		print('%s says bye.'%self.name)
		Person.population -= 1

		if Person.population == 0:
			print("I am the last one")
		else:
			print('There are still %d person left.'%Person.population)

	def howMany(self):
		'''Prints the current population.'''
		if Person.population == 1:
			print('I\'m the only person here.')
		else:
			print('We have %d persons here.'%Person.population)


jy = Person("Jiang Yu")
jy.sayHello()
jy.howMany()
print()

mj = Person("Ma Jun")
mj.sayHello()
mj.howMany()
print()

jy.sayHello()
jy.howMany()
print()

print()
jy.sayHello()
jy.howMany()

