def my_decorator(func):
    def wrapper():
        print("Before function runs")
        func()
        print("After function runs")
    return wrapper

def say_hello():
    print("Hello!")

say_hello = my_decorator(say_hello)

say_hello()

#Using @

def my_decorator(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper

@my_decorator
def greet():
    print("Hi")

greet()

#with Arguments
def my_decorator(func):
    def wrapper(name):
        print("before")
        func(name)
        print("after")
    return wrapper

@my_decorator
def greet(name):
    print(f"Hello {name}")

greet("Shreya")

#Using *args, **kwargs

def log(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@log
def add(a, b):
    return a + b

print(add(2, 3))
    
#@staticmethod

class MathUtils:

    @staticmethod
    def add(a,b):
        return a+b
print(MathUtils.add(2,3))

#@classmethod

class Student:
    school = "ABC School"

    @classmethod
    def change_school(cls, name):
        cls.school = name

Student.change_school("XYZ School")

print(Student.school)  # XYZ School

#example

class User:
    users = []

    def __init__(self, name):
        self.name = name
        User.users.append(name)

    @classmethod
    def total_users(cls):
        return len(cls.users)

    @staticmethod
    def is_valid_name(name):
        return name.isalpha()

u1 = User("Nandani")
u2 = User("Niharika")

print(User.total_users())          # 2
print(User.is_valid_name("123"))   # False