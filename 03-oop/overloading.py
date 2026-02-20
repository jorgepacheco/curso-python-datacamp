
class Phone:
  def __init__(self, number):
    self.number = number


class BankAccount:
  # Modify to initialize a number attribute
  def __init__(self, number, balance=0):
    self.balance = balance
    self.number = number

  def withdraw(self, amount):
    self.balance -= amount

  # Define __eq__ that returns True if the number attributes are equal
  def __eq__(self, other):
    return (self.number == other.number) and (type(self) == type(other))

# Create accounts and compare them
acct1 = BankAccount(123, 1000)
acct2 = BankAccount(123, 1000)
acct3 = BankAccount(456, 1000)
print(acct1 == acct2)
print(acct1 == acct3)


acct = BankAccount(873555333)
pn = Phone(873555333)

# Check if the two objects are equal
print(acct == pn)

print(pn == acct)


class Employee:
    def __init__(self, name, salary=30000):
        self.name, self.salary = name, salary

    # Add the __repr__() method
    def __repr__(self):
        return f"Employee('{self.name}', {self.salary})"
    # Add the __str__() method
    def __str__(self):
      emp_str = f"""Employee name: {self.name}
Employee salary: {self.salary}"""
      return emp_str

emp1 = Employee("Amar Howard", 30000)
print(repr(emp1))
emp2 = Employee("Carolyn Ramirez", 35000)
print(repr(emp2))

print(emp1)
print(emp2)