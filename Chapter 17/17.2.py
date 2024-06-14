class Kangaroo:

	def __init__(self):
		self.pouch_contents = []

	def __str__(self):
		return str(self.pouch_contents)

	def put_in_pouch(self, obj):
		""" Takes any object (obj) and adds to the pouch content list """
		self.pouch_contents.append(obj)

kanga = Kangaroo()
roo = Kangaroo()

kanga.put_in_pouch(roo)
print(kanga)