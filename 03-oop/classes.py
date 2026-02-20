print("Hello from 03-oop!")

ratio = 12 / 8

# List all attributes and methods for the ratio object
#print(dir(ratio))

# List all attributes and methods for the float class
#print(dir(float))

class Customer:
  def set_name(self, name):
    self.name = name

  def identify(self):
    print(f"I am a customer and my name is {self.name}")

customer = Customer()
customer.set_name("Alice")
customer.identify()

# Create an empty class Employee
class EmployeeEmpty:
  pass
employee =  EmployeeEmpty()

class Employee:
  def __init__(self, name, salary=0):
    self.name = name
    # Check if salary is positive
    if salary >= 0:
      self.salary = salary
    else:
      self.salary = 0
      print("Invalid salary!")

  def give_raise(self, amount):
    self.salary += amount

  def monthly_salary(self):
    return self.salary / 12

emp = Employee("Korel Rossi", -1000)
print(emp.name)
print(emp.salary)

# Define and initialize the Calculator class
class Calculator:
  def __init__(self, num_one, num_two):
    self.num_one = num_one
    self.num_two = num_two

  # Create the addition method
  def addition(self):
    return self.num_one + self.num_two

  # Create the subtraction method
  def subtraction(self):
    return self.num_one - self.num_two

  # Create the multiplication method
  def multiplication(self):
    return self.num_one * self.num_two

calc = Calculator(10, 5)
print(calc.addition())

class Player:
  MAX_POSITION = 10

  # Define a constructor
  def __init__(self, position):

    # Check if position is less than the class-level attribute value
    if position <= Player.MAX_POSITION:
      self.position = position

    # If not, set equal to the class-level attribute
    else:
      self.position = Player.MAX_POSITION

# Create a Player object, p, and print its MAX_POSITITON
p = Player(6)
print(p.MAX_POSITION)
print(p.position)


class Person:
  CURRENT_YEAR = 2024
  def __init__(self, name, age):
    self.name = name
    self.age = age

  # Add a class method decorator
  @classmethod
  # Define the from_birth_year method
  def from_birth_year(cls, name, birth_year):
    # Create age
    age = cls.CURRENT_YEAR - birth_year
    # Return the name and age
    return cls(name, age)

bob = Person.from_birth_year("Bob", 1990)

print(bob.name)
print(bob.age)

class BetterDate:
  def __init__(self, year, month, day):
    self.year, self.month, self.day = year, month, day

  # Define a class method from_str
  @classmethod
  def from_str(cls, datestr):
    # Split the string at "-"
    parts = datestr.split("-")
    year, month, day = int(parts[0]), int(parts[1]), int(parts[2])
    # Return the class instance
    return cls(year, month, day)

# Create the xmas object
xmas = BetterDate.from_str("2024-12-25")
print(xmas.year)
print(xmas.month)
print(xmas.day)