import string

def average(values):
    average_value = sum(values) / len(values)
    rounded_average = round(average_value, 2)
    return rounded_average

prepared_values = [1.23, 2,23, 3.22]
print("Average:", average(prepared_values))

test_durations = [245.50, 189.99, 312.75, 156.20, 428.90, 201.35, 167.80]

 # Complete the function
def test_report(durations):
    num_tests = len(durations)

    # Calculate total test time
    total_time = sum(durations)

    print("=== Test Report ===")
    print("Total Tests: ", num_tests)
    print("Total Execution Time (s): ", total_time)

# Generate the report for recent test runs
test_report(test_durations)

def validate_password(password):
    # Check if password is at least 8 characters long
    if len(password) >= 8:
        # Check if password contains a special character
        for char in password:
            if char in string.punctuation:
                return True
    return False

# Call the function and store the result
is_valid = validate_password("user_password")
print("Is the password valid? ", is_valid)

## Argumentos por defecto
def greet(name="Guest"):
    return f"Hello, {name}!"
print(greet())  # Output: Hello, Guest!
print(greet("Alice"))  # Output: Hello, Alice!

product = 'Wireless Mouse'

# Define clean_text function
def clean_text(text, lower=True):
    clean_text = text.replace(' ', '_')
    if lower == False:
        return clean_text
    else:
        # Apply lowercase transformation
        return clean_text.lower()

# Test with default behavior
print(clean_text(product))

original_price = 899.99

# Define the function with default arguments
def calculate_discount(price, discount_percent=15, round_result=True):
    discounted_price = price - (price * (discount_percent / 100))

    if round_result == True:
        # Round the result to two decimal places
        return round(discounted_price, 2)
    else:
        return discounted_price

# Call the function with keyword arguments
final_price = calculate_discount(price=original_price, discount_percent=25, round_result=False)
print(final_price)

## docstrings
def calculate_discount(price, discount_percent=15, round_result=True):
    # Add a single-line docstring
    """Calculate the discounted price of a product."""

    discounted_price = price - (price * (discount_percent / 100))
    if round_result == True:
        return round(discounted_price, 2)
    else:
        return discounted_price

# Access the docstring
print(calculate_discount.__doc__)

## Arbitrary arguments
# Define a function called concat
def concat(*args):
  """Concatenates multiple string arguments with spaces between them."""

  result = ""

  # Iterate over the Python args tuple
  for arg in args:
    result += " " + arg
  return result

# Call the function
print(concat("Python", "is", "great!"))

# Define a function called concat
def concat(**kwargs):
  """Concatenates keyword arguments into a single string with spaces."""

  result = ""

  # Iterate over the Python kwargs
  for kwarg in kwargs.values():
    result += " " + kwarg
  return result

# Call the function
print(concat(start="Python", middle="is", end="great!"))

# Lambda functions
# Define a lambda function to calculate the area of a circle
area_of_circle = lambda radius: 3.14159 * (radius ** 2)
# Call the lambda function
print("Area of circle with radius 5: ", area_of_circle(5))

colleagues = ["Sarah Martinez", "Michael Chen", "Emily Brown"]

# Apply the lambda function to each colleague's name
cleaned = map(lambda x: x.replace(" ", "_").lower(), colleagues)
print(cleaned)
# Convert map object to list
cleaned_list = list(cleaned)
print(cleaned_list)