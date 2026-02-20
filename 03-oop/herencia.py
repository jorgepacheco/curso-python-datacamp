class Employee1:
    MIN_SALARY = 30000

    def __init__(self, name, salary=MIN_SALARY):
        self.name = name
        if salary >= Employee1.MIN_SALARY:
            self.salary = salary
        else:
            self.salary = Employee1.MIN_SALARY

    def give_raise(self, amount):
        self.salary += amount

# Define a new class Manager inheriting from Employee
class Manager1(Employee1):
    # Add a keyword to leave this class empty
    pass

# Define a Manager object
mng = Manager1("Debbie Lashko", 86500)

# Print mng's name
print(mng.name)

class Employee:
  def __init__(self, name, salary=30000):
    self.name = name
    self.salary = salary

  def give_raise(self, amount):
    self.salary += amount

class Manager(Employee):
  # Add a constructor
  def __init__(self, name, salary=50000, project=None):

    # Call the parent's constructor
    Employee.__init__(self, name, salary)

    # Assign project attribute
    self.project = project

  def display(self):
    print("Manager ", self.name)

  # Add a give_raise method
  def give_raise(self, amount, bonus=1.05):
    new_amount = amount * bonus
    Employee.give_raise(self, new_amount)

# Create a Manager object
mng = Manager("Debbie Lashko", 86500, "Project X")
# Print mng's name and project
print(mng.name)
print(mng.project)

mngr = Manager("Ashta Dunbar", 78500)
mngr.give_raise(2000, bonus=1.03)
print(mngr.salary)