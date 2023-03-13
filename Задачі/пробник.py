principal = 1000
rate = 1.05
numyears = 5
year = 1
while year <= numyears:
    principal = principal * rate
    print(year, round(principal, 2))
    year += 1