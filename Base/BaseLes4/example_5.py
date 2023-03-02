def divide(n_1, n_2):
    return n_1 / n_2


def print_divide(n_1, n_2):
    try:
        result = divide(n_1, n_2)
        print(f"Divide result: {result}")
    except:
        print("Error in numbers dividing!")


def run_divide(number_1, number_2):
    print("Dividing numbers")
    print_divide(number_1, number_2)


if __name__ == "__main__":
    run_divide(10, 0)
    run_divide(10, 2)
