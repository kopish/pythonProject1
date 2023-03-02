# example_3.py

class Bird:    
	TYPE = "Bird"    

	def fly(self):        
		print(f"I am a {self.TYPE} and I can fly!")

class Horse:    
	TYPE = "Horse"    

	def run(self):        
		print(f"I am a {self.TYPE} and I can run!")

class Pegas(Bird, Horse):    
	pass

my_home_pegas = Pegas()
my_home_pegas.run()
my_home_pegas.fly()
