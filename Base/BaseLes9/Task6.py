with open('file.txt', 'r') as f:
    result = sum(map(float, f))
print(result)
