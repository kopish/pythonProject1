FIRST_NUMBER = 8
SECOND_NUMBER = 2
THIRD_NUMBER = 10

# Variant №1
print(FIRST_NUMBER + SECOND_NUMBER + THIRD_NUMBER)

# Variant №2
numbers_to_sum = [FIRST_NUMBER, SECOND_NUMBER, THIRD_NUMBER]
print(sum(numbers_to_sum))

# Variant №3
def sum_numbers_list(numbers_list, current_value=0):    
	new_number = numbers_list.pop()    
	new_value = current_value + new_number    

	if len(numbers_list) != 0:        
		return sum_numbers_list(numbers_list, new_value)    
	else:        
		return new_value

print(sum_numbers_list(numbers_to_sum))
