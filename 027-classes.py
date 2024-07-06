from tools import separator, section

section('basic class')
class SmartForm:
	level = "medium"
sf = SmartForm()
print(sf.level)

section('class with init')
class Person:
	def __init__(self, firstName, lastName, age) -> None:
		self.firstName = firstName
		self.lastName = lastName
		self.age = age
	def display(self) -> str:
		return f"{p.firstName} {p.lastName} is {p.age} years old."
p = Person("Peter", "Stodio", 34)
print(p.display())




















section('class with __str__')
class Person:
	def __init__(self, firstName, lastName, age) -> None:
		self.firstName = firstName
		self.lastName = lastName
		self.age = age
	def __str__(self) -> str:
		return f"{p.firstName} {p.lastName} is {p.age} years old."
p = Person("Peter", "Stodio", 34)
print(p)
