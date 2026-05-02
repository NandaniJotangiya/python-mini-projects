class Student:

    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def greet(self):
        print(f"Hi,my name is {self.name} and my age is {self.age}")

s1 = Student("Nandani",23)

print(s1.name)
s1.greet

#Encapsulation

class BankAccount:

    def __init__(self,balance):
        self.__balance = balance # Private variable

    def deposite(self,amount):
        self.__balance += amount
        
    def getBalance(self):
        return self.__balance

acc = BankAccount(5000)

acc.deposite(2000)
print(acc.getBalance())

#Inheritance:

class Animal:
    def speak(self):
        print("Animal Speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

d = Dog()
d.speak()
d.bark()

#Polymorphism:

class Dog:
    def sound(self):
        print("Bark")

class Cat:
    def sound(self):
        print("Meow")

animals = [Dog(), Cat()]

for a in animals:
    a.sound()

#Abstraction:

from abc import ABC, abstractmethod

class Vehicle(ABC):
    
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car starts")

c = Car()
c.start()
