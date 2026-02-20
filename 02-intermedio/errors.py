import requests
# Define the sales list
sales = [125.97, 84.32, 99.78, 154.21, 78.50, 83.67, 111.13]

# Print the sales list
print(sales)

requests.get(url="https://app.datacamp.com")

def clean_text(text):
  # Attempt to clean the text
  try:
    return text.replace(" ", "_").lower()
  # Run this code if an error occurs
  except:
    print("The clean_text() function expects a string as an argument, please check the data type provided!")

clean_text(187)

def clean_text2(text):
  # Check the data type
  if type(text) == str:
    return text.replace(" ", "_").lower()
  else:
    # Return a TypeError error if the wrong data type was used
    raise TypeError("The clean_text() function expects a string as an argument, please check the data type provided!")

clean_text2("User Name 187")
##clean_text2(12)