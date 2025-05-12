# 1. Using self
# Assignment:
# Create a class Student with attributes name and marks.
# Use the self keyword to initialize these values via a constructor.
# Add a method display() that prints student details.

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Name: {self.name}, Marks: {self.marks}")

s1 = Student("Ali", 90)
s1.display()
print(s1.name)






# 2. Using cls
# Assignment:
# Create a class Counter that keeps track of how many objects have been created. 
# Use a class variable and a class method with cls to manage and display the count.

class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

    @classmethod
    def show_count(cls):
        print("Objects created:", cls.count)

c1 = Counter()
c2 = Counter()
Counter.show_count()




# 3. Public Variables and Methods
# Assignment:
# Create a class Car with a public variable brand and a public method start().
# Instantiate the class and access both from outside the class.


class Car:
    def __init__(self,brand):
        self.brand=brand

    def start(self):
        print(f"{self.brand} car started!")

c = Car("Toyota")
print(c.brand)
c.start()



# 4. Class Variables and Class Methods
# Assignment:
# Create a class Bank with a class variable bank_name.
# Add a class method change_bank_name(cls, name) that allows changing the bank name.
# Show that it affects all instances.


class Bank:
    bank_name="State Bank"

    @classmethod
    def change_bank_name(cls,name):
        cls.bank_name = name

b1 = Bank()
b2 = Bank()
print(b1.bank_name)
Bank.change_bank_name("New Bank")
print(b2.bank_name)


# 5. Static Variables and Static Methods
# Assignment:
# Create a class MathUtils with a static method add(a, b) that returns the sum.
# No class or instance variables should be used.


# --------explanation
# Static method na to object ko access karta hai na class ko. 
# Bas ek normal function hota hai class ke andar.
# object ki zarurat nahi.
#Is method ki wja se hm ise direct access ke kr skty hain bger kisi variable me store kr skty
# hain self use krny ki bhi zrurt nhi hoti 

class MathUtils:
    @staticmethod
    def add(a,b):
        return a+b
print(MathUtils.add(3, 5))



# 6. Constructors and Destructors
# Assignment:
# Create a class Logger that prints a message when an object is created (constructor) and another message when it is destroyed (destructor).


class Logger:
    def __init__(self):
        print("Object created.")

    def __del__(self):
        print("Object destroyed.")

log = Logger()
del log




# 7. Access Modifiers: Public, Private, and Protected
# Assignment:
# Create a class Employee with:

# a public variable name,

# a protected variable _salary, and

# a private variable __ssn.

# Try accessing all three variables from an object of the class and document what happens.

class Employee:
    def __init__(self):
            self.name = "Ahmed"
            self._salary = 5000
            self.__ssn = "123-45-6789"

e = Employee()
print(e.name)
print(e._salary)


# 8. The super() Function
# Assignment:
# Create a class Person with a constructor that sets the name.
# Inherit a class Teacher from it, add a subject field, 
# and use super() to call the base class constructor.


class Person:
    def __init__(self,name):
        self.name = name

class Teacher(Person):
    def __init__(self,name,subject):
        super().__init__(name)
        self.subject=subject

t=Teacher("Sara", "Math")
print(t.name,t.subject)



# 09. Abstract Classes and Methods
# Assignment:
# Use the abc module to create an abstract class Shape with an abstract method area().
# Inherit a class Rectangle that implements area().

# ------------Explanation

# --Abstract class aik aisi class hoti hai jo adhoori hoti hai — usme kuch methods sirf declare hote hain, 
# lekin unka kaam likha nahi hota.
# --Tum abstract class ka object nahi bana sakti — sirf usko inherit karke poora kaam child class mein likhna padta hai.

from abc import  ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def area(self):
        return self.width*self.height

r = Rectangle(4,5)
print(r.area())



# 10. Instance Methods
# Assignment:
# Create a class Dog with instance variables name and breed.
# Add an instance method bark() that prints a message including the dog's name.

class Dog:
    def __init__(self,name,breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} is barking!")

d = Dog("Bruno", "Bulldog")
d.bark()



# 11. Class Methods
# Assignment:
# Create a class Book with a class variable total_books.
# Add a class method increment_book_count() to increase the count when a new book is added.

class Book:
    total_books = 0

    @classmethod
    def increment_book_count(cls):
        cls.total_books +=1

Book.increment_book_count()
Book.increment_book_count()
print(Book.total_books)



# 12. Static Methods
# Assignment:
# Create a class TemperatureConverter with a static method celsius_to_fahrenheit(c) that returns
# the Fahrenheit value.


# ---------explanation
# Humne @staticmethod is liye use kiya:
# Kyunke temperature convert karna sirf input aur formula ka kaam hai.

# Isme kisi object ka data (jaise self.temp) use nahi ho raha.

# Na class variable (like cls.unit) use ho raha.


class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c*9/5) +32

print(TemperatureConverter.celsius_to_fahrenheit(25))



# 13. Composition
# Assignment:
# Create a class Engine and a class Car.
#  Use composition by passing an Engine object to the Car class during initialization. Access a method of the Engine class via the Car class.

class Engine:
    def start(self):
        print("Engine started.")

class Car:
    def __init__(self, engine):
        self.engine = engine

    def start_car(self):
        self.engine.start()

e = Engine()
c = Car(e)
c.start_car()




# 14. Aggregation
# Assignment:
# Create a class Department and a class Employee.
# Use aggregation by having a Department object store a reference to an Employee object that exists independently of it.

# -------Explanation

# Aggregation mein ek object doosre object ka reference rakhta hai

class Employee:
    def __init__(self,name):
        self.name = name

class Department:
    def __init__(self,emp):
        self.emp = emp

e = Employee("Ali")
d= Department(e)
print(d.emp.name)



# 15. Method Resolution Order (MRO) and Diamond Inheritance
# Assignment:
# Create four classes:

# A with a method show(),

# B and C that inherit from A and override show(),

# D that inherits from both B and C.

# Create an object of D and call show() to observe MRO.

class A:
    def show(self):
        print("A")

class B(A):
    def Show(self):
        print("B")

class C(A):
    def show(self):
        print("C")

class D(B,C):
    pass

d = D()
d.show()



# 16. Function Decorators
# Assignment:
# Write a decorator function log_function_call that prints "Function is being called" before a function executes.
# Apply it to a function say_hello().

def log_function_call(func):
    def wrapper():
        print("Function is being called")
        func()
    return wrapper

@log_function_call
def say_hello():
    print("Hello!")

say_hello()


