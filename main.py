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


