ingredent = "flour"
ingredent_quantity = 2

print("The ingredent is " + ingredent)
print("The quantity is " + str(ingredent_quantity))

# Float
pi = 3.1416
print("The value of pi is " + str(pi))
# Boolean
is_raining = False
print("Is it raining? " + str(is_raining))

# type function
print(type(ingredent))
print(type(ingredent_quantity))
print(type(pi))
print(type(is_raining))

# Track if you have pasta at home
has_pasta = True

# Track if you have garlic
has_garlic = False

print(has_pasta)
print(has_garlic)

## Working with strings
first_name = "John"

##Multi-line string
multi_line_string = """This is a multi-line string.
It can span multiple lines.
It is useful for long text."""

print(multi_line_string)

# str function
number = 42
number_as_string = str(number)
print("The number as a string is: " + number_as_string)

#replace method
greeting = "Hello, World!"
new_greeting = greeting.replace("World", "Python")
print(new_greeting)

pasta_type = "pasta"

# Update pasta type to be more specific
pasta_type = pasta_type.replace("pasta", "fusilli pasta")

ingredient_one = "BASIL"

# Standardize ingredient_one to lowercase
ingredient_one = ingredient_one.lower()

print(pasta_type)
print(ingredient_one)

###### Listas
shopping_list = ["flour", "sugar", "eggs", "milk"]
print(shopping_list)
print(type(shopping_list))
print("The first item in the shopping list is: " + shopping_list[0])
print("The second item in the shopping list is: " + shopping_list[1])

## Imprime el último elemento de la lista
print("The last item in the shopping list is: " + shopping_list[-1])

## Imprimer un rango de elementos
print("The first three items  " + str(shopping_list[0:3]))

# Create a list of ingredients
ingredients = ["fusilli", "tomatoes", "garlic", "basil", "olive oil", "salt"]

# Create a list of ingredient quantities
quantities = [500, 400, 15, 20, 30, 10]

print(ingredients)
print(quantities)

# Obtener los ingredientes alternos de la lista
alternate_ingredients = ingredients[::2]
print("Alternate ingredients: " + str(alternate_ingredients))

# Dictionaries
# Create the recipe dictionary
recipe = {"olive_oil": 30,
# Add garlic
          "garlic": 15,
# Add tomatoes
          "tomatoes": 400}

# Add basil to the recipe dictionary
recipe["basil"] = 20

print(recipe)

# Get all ingredient names
ingredient_names = recipe.keys()

# Get all quantities
quantities = recipe.values()

# Get all key-value pairs
recipe_items = recipe.items()

print("Ingredient names:", ingredient_names)
print("Quantities:", quantities)
print("Recipe items:", recipe_items)

### Conjuntos y tuplas
# Create a tuple
cup_conversion = (1,240)

# Check the type
print(type(cup_conversion))

unique_ingredients = set(ingredients)

print(unique_ingredients)
print(type(unique_ingredients))
print(sorted(unique_ingredients))

# Condicionales
temperature = 25
if temperature > 30:
    print("It's a hot day!")
elif temperature > 20:
    print("It's a nice day!")
else:
    print("It's a bit cold today.")

## Loops
# For loop to print each ingredient
ingredients = ["fusilli", "tomatoes", "garlic", "basil", "olive oil", "salt"]

# Loop through each ingredient in the list
for item in ingredients:
    print(item)

#range function to print numbers from 1 to 5
for i in range(1, 6):
    print(i)

recipe = {
    "tomatoes": 400,
    "basil": 20,
    "garlic": 15,
    "olive oil": 15,
    "salt": 7
}

# Loop through the recipe dictionary items
for ingredient, qty in recipe.items():
    # Calculate the scaled quantity by multiplying by 2
    scaled_qty = qty * 2
    print(ingredient, ":", scaled_qty, "g")

pantry_stock = {'pasta': 100, 'tomatoes': 1500, 'basil': 20, 'garlic': 10, 'olive_oil': 10, 'salt': 150}

# Create an empty shopping list
shopping_list = []
# Loop through each ingredient and required quantity
for ingredient, required_qty in recipe.items():
    # Check if we need more than what we have
    if required_qty > pantry_stock[ingredient]:
        # Add the ingredient to our shopping list
        shopping_list.append(ingredient)

# Display the shopping list
print("Shopping list:", len(shopping_list), "items:", shopping_list)