# example_1.py

class Cat:    
	def __init__(self, name):        
		self.name = name    
	
	def say_meow(self):        
		print(f"{self.name}: Meow!")


class Kitty(Cat):    
	pass


my_cat = Cat("Black")
my_kitty = Kitty("Gray")

my_cat.say_meow()
my_kitty.say_meow()
