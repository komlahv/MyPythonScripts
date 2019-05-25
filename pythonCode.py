import math
from datetime import datetime

variable1 = 10
product = 2 * 3
remainder = 1398 % 11

print("hello world")

# .............................................................
# rainfall variable lesson
january_to_june_rainfall = 1.93 + 0.71 + 3.53 + 3.41 + 3.69 + 4.50
annual_rainfall = january_to_june_rainfall

july_rainfall = 1.05
annual_rainfall += july_rainfall

august_rainfall = 4.91
annual_rainfall += august_rainfall

september_rainfall = 5.16
october_rainfall = 7.20
november_rainfall = 5.06
december_rainfall = 4.06

annual_rainfall += september_rainfall + \
                   october_rainfall + november_rainfall + december_rainfall

# .............................................................
# data types lesson
cucumbers = 1
price_per_cucumber = 3.25
total_cost = cucumbers * price_per_cucumber
print(total_cost)
# make sure number is float to avoid rounding of numbers
quotient1 = 7. / 2
# the value of quotient1 is 3.5
quotient1 = float(7) / 2
# the value of quotient1 is 3.5

# example of float vs integer
cucumbers = 100
num_people = 6
whole_cucumbers_per_person = cucumbers / num_people
print(whole_cucumbers_per_person)

float_cucumbers_per_person = float(cucumbers) / num_people
print(float_cucumbers_per_person)

# multi line strings
address_string = """136 Whowho Rd
Apt 7
Whosville, WZ 44494"""

# .............................................................
# convert
skill_completed = "Python Syntax"
exercises_completed = 13
# The amount of points for each exercise may change, because points don't exist yet
points_per_exercise = 5
point_total = 100

point_total += exercises_completed * points_per_exercise
print("I got " + str(point_total) + " points!")

# .............................................................
# time...vs code sent import statement to the top
now = datetime.now()

current_year = now.year
current_month = now.month
current_day = now.day

current_hour = now.hour
current_minute = now.minute
current_second = now.second

# the standalone % operator after the string will fill the %02d and %04d placeholders in the string on the left with the numbers and strings in the parentheses on the right.
print('%02d-%02d-%04d' % (now.month, now.day, now.year))
print('%02d:%02d:%02d' % (now.hour, now.minute, now.second))
# will print the current date as mm-dd-yyyy

# .............................................................
# conditions
print('Welcome to the Pig Latin Translator!')
original = input("Enter a word: ")
# original = "hi2"

if len(original) > 0 and original.isalpha():
    # Run this block.
    # Maybe print something?
    print(original)
elif not original.isalpha():
    # Run this block.
    print("Use only letters")
elif original.isalpha():
    # use pass as placeholder where python expects an expression
    pass
else:
    # That string must have been empty.
    # Start coding here!
    print("bad")


# .............................................................
# functions


def tax(bill):
    """Adds 8% tax to a restaurant bill."""
    bill *= 1.08
    print("With tax: %f" % bill)
    return bill


def tip(bill):
    """Adds 15% tip to a restaurant bill."""
    bill *= 1.15
    print("With tip: %f" % bill)
    return bill


meal_cost = 100
meal_with_tax = tax(meal_cost)
meal_with_tip = tip(meal_with_tax)

# .............................................................
# tuples, lists and doctionaries
tupleVar = ("same", "forever")
list_name = ["apple", "orange"]
dict1 = {"a": "benz", "b": "bmw"}

if "a" in dict1:
    print(dict1["a"])

# .............................................................
# loops
count = 0
while count < 5:
    print("Hello, I am a while and count is" + str(count))
    count += 1


# .............................................................
# classes


class ShoppingCart(object):
    """Creates shopping cart objects
    for users of our fine website."""

    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.items_in_cart = {}

    def add_item(self, product, price):
        """Add product to the cart."""
        if not product in self.items_in_cart:
            self.items_in_cart[product] = price
            print(product + " added.")
        else:
            print(product + " is already in the cart.")

    def remove_item(self, product):
        """Remove product from the cart."""
        if product in self.items_in_cart:
            del self.items_in_cart[product]
            print(product + " removed.")
        else:
            print(product + " is not in the cart.")


my_cart = ShoppingCart("Victor")
my_cart.add_item("Beans", 2)


# .............................................................
# Inheritance,    putting customer as the class parameter lets it use methods from the customer class

class Customer(object):
    """Produces objects that represent customers."""

    def __init__(self, customer_id):
        self.customer_id = customer_id

    def display_cart(self):
        print("I'm a string that stands in for the contents of your shopping cart!")


class ReturningCustomer(Customer):
    """For customers of the repeat variety."""

    def display_order_history(self):
        print("I'm a string that stands in for your order history!")


monty_python = ReturningCustomer("ID: 12345")
monty_python.display_cart()
monty_python.display_order_history()


# Inheritance example 2
class Triangle(object):
    number_of_sides = 3

    def __init__(self, angle1, angle2, angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3

    def check_angles(self):
        if (self.angle1 + self.angle2 + self.angle3 == 180):
            return True
        else:
            return False


my_triangle = Triangle(90, 30, 60)
print(my_triangle.number_of_sides)
print(my_triangle.check_angles())


class Equilateral(Triangle):
    angle = 60

    def __init__(self):
        self.angle1 = self.angle
        self.angle2 = self.angle
        self.angle3 = self.angle


# .............................................................
# override

class Employee(object):
    """Models real-life employees!"""

    def __init__(self, employee_name):
        self.employee_name = employee_name

    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 20.00


# Add your code below!


class PartTimeEmployee(Employee):
    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 12.00


# use super to call method from parent/super class if you override it
class Employee2(object):
    """Models real-life employees!"""

    def __init__(self, employee_name):
        self.employee_name = employee_name

    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 20.00


# Add your code below!


class PartTimeEmployee2(Employee2):
    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 12.00

    def full_time_wage(self, hours):
        return super(PartTimeEmployee2, self).calculate_wage(hours)


milton = PartTimeEmployee2("John")
print(milton.full_time_wage(10))

# writing to files
# .............................................................
my_list = [i ** 2 for i in range(1, 11)]

my_file = open("output.txt", "w")

# Add your code below!
for item in my_list:
    my_file.write(str(item) + "\n")
my_file.close()

# read from file
# .............................................................
my_file = open("output.txt", "r")

print(my_file.read())
my_file.close()
