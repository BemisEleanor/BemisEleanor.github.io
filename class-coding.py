class dogs():
	def __init__(self,name,size,potential_for_weight_gain):
		self.name = name
		self.size = size
		self.potential_for_weight_gain = potential_for_weight_gain
	
	def call(self):
		print("come here " + self.name)

	def bark(self):
		print("woof")

	def is_fat(self):
		if self.potential_for_weight_gain == "high potential for weight gain":
			print(self.name + " " + "is too fat")
		else:
			print(self.name +" "+ "is not too fat!")

pug= dogs("pug","small","high potential for weight gain")
german_shepard = dogs("german_shepard","big","low potential for weight gain")
beagle = dogs('beagle','medium','high potential for weight gain')

beagle.call()
beagle.bark() 
beagle.is_fat()








