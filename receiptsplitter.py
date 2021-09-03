class Person:
	def __init__(self, name):
		self.name = name
		self.items = []

	def addItem(self, price):
		self.items.append(price)

	@property
	def total(self):
		return sum(self.items)
	

def addPerson(name):
	newPerson = Person(name)
	while True:
		price = input("Type in price of new item or 'stop': ")
		if price.lower() == "stop":
			break
		try:
			newPerson.addItem(float(price))
		except ValueError:
			print("Not a number")
	return newPerson


def run():
	people = []
	while True:
		newName = input("Enter a name or 'stop': ")
		if newName.lower() == "stop":
			break
		people.append(addPerson(newName))
	while True:
		total = input("Enter total with all fees and tip: ")
		try:
			total = float(total)
			break
		except:
			print("Not a number")
	tot = 0
	for person in people:
		tot+=person.total
	for person in people:
		print(f"{person.name}: ${round(person.total/tot*total, 2)}")

run()