def nonrecursive(n):
    result = 1
    for multiplier in range(2, n + 1):
        result *= multiplier
    return result


def recursive_factorial(n):
    if n == 0:
        return 1
    else:
        return n * recursive_factorial(n - 1)


print(recursive_factorial(5))
print(nonrecursive(5))
