class Human:
    def __init__(self, age, name, gender):
        self.age = age
        self.name = name
        self.gender = gender

    def get_name(self):
        return self.name

    def get_age_name(self):
        return self.age, self.get_name()

    def say_hello(self):
        print(f'Hello, I am {self.age}')


#human_1 = Human(age=25, name="Alex", gender='male')

#human_1.say_hello()


class HumanExtended(Human):
    def __init__(self, age, name):
        super().__init__(age)
        self.name = name


#human2 = HumanExtended(age=58, name='John')
#human2.say_hello()



class A():
    def __init__(self):
        self.a = 10


class B():
    def __init__(self):
        self.b = 5


class C(A, B):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)


c = C()
print(c.a)
print(c.b)