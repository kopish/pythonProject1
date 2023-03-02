# example_3.py

class Person:
    def _get_secret(self):
        print("It is my big secret!")

    def __get_the_biggest_secret(self):
        print("Quieter! It is my biggets secret!")


me = Person()
me._Person__get_the_biggest_secret()
