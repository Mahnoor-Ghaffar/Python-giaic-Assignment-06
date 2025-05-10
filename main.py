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
