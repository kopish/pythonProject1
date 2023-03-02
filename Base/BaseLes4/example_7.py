NOT_ALLOWED_SYMBOLS = ['/', ';', '*', '%']


class UserInputError(Exception):
    pass


def has_string_symbols(string, symbols):
    for symbol in symbols:
        if symbol in string:
            return True

    return False


def user_input_check_loop():
    while True:
        user_string = input("Enter a string to check: ")
        if has_string_symbols(user_string, NOT_ALLOWED_SYMBOLS):
            raise UserInputError('You used not allowed symbols!')
            # raise UserInputError()


if __name__ == "__main__":
    user_input_check_loop()
