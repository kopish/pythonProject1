def stairs(n):
    if n == 1:
        return 1
    return stairs(n - 1) + n


print(stairs(5))