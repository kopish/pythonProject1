# example_5.py

class MathBase:    
	def math_operation(self, number_1, number_2, operation):       

		if operation == "-":            
			return number_1 - number_2        
		elif operation == "+":            
			return number_1 + number_2


class MathUpgrated(MathBase):    
	def math_operation(self, number_1, number_2, operation):        
		if operation in ["+", "-"]:            
			parent_class_object = super()            
			result = parent_class_object.math_operation(number_1, number_2, operation)            
			return result        
		elif operation == "*":            
			return number_1 * number_2        
		elif operation == "/":            
			return number_1 / number_2        

my_math = MathUpgrated()

print(my_math.math_operation(4, 2, "+")) # ==> 6
print(my_math.math_operation(4, 2, "-")) # ==> 2
print(my_math.math_operation(4, 2, "/")) # ==> 2.0
print(my_math.math_operation(4, 2, "*")) # ==> 8
