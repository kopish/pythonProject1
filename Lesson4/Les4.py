price = float(input("Enter the cost of the goods (press 0 for the check): "))
total_cost = 0
qua_goods = 0
while price != 0:
    total_cost += price
    qua_goods += 1
    price = float(input("Enter the cost of the goods (press 0 for the check): "))
print("The total number of goods", qua_goods)
print("Total cost is", round(total_cost, 2))
print("The average cost of goods", total_cost / qua_goods)
