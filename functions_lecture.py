# TIME TO GET FUNKY
# Python Functions
# Built-In Functions
# .method()
# function()

# Examples of Built-In Functions
# sum()
# round()
# min()
# max()
# input()

# sum get the sum of a list of integers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(sum(numbers))

# min() grabs the smallest item from a list
print(min(numbers))

# max() grab the largest item from a list
print(max(numbers))

vegetables = ["Tomato", "Potato", "asparagus", "cucumber", "Artichoke"]
print(min(vegetables))
print(max(vegetables))
print(sorted(vegetables))

# round() round to the nearest number depending on if we are greater or less than .5
print(round(3.6))
print(round(11.4))


# ==================== BUILDING CUSTOM FUNCTIONS PYTHON =============================

# defining a function 
# def name_of_our_function():
def function_name():
    pass

# defining a function and adding functionality
def greet_user():
    print("Hello, user!")

# calling a function
greet_user()

# paramters and arguments
# parameter is a placeholder for a argument inside of a function
# argument is what fulfills the place the parameter is holding

#              parameter
def greet_user(user):
    #              using the parameter in the function
    print(f"Hello, {user}!")

# calling a function with an argument
# arguments go in the parantheses when the function is called
greet_user("Mega Man") #mega man is a cool robot with a bunch of fun video games
greet_user("Winter")
greet_user("Andy")
greet_user("Karen")

# cooking some pasta
def cook_pasta(sauce):
    print(f"Cooking some pasta with {sauce} sauce and some SPICY MEATABALLS")

cook_pasta("prego")
cook_pasta("alfredo")
cook_pasta("vodka")


# we are not limited to just one parameter/argument
def make_sandwich(bread, filling):
    print(f"I'm making a delicious sandwich with {bread} bread and {filling}")

make_sandwich("rye", "pastrami")
make_sandwich("whole grain wheat", "peanut butter and jelly")
make_sandwich("German", "nuts")
make_sandwich("normal white", "meatballs")
make_sandwich("normal white", "bacon,lettuce, tomato")
# keyword arguments
# keyword arguments must follow positional arguments
# if we have all keyword arguments, the position no longer matters
make_sandwich(filling="Salami", bread="wheat")

def make_sandwich(bread, filling, condiment):
    print(f"I'm making a delicious sandwich with {bread} bread and {filling} with {condiment}")

make_sandwich("bread", "ham", "mustard")


# *args any number of arguments
# make a sandwich with args
def make_sandwich(*general_sandwich_stuff):
    print(general_sandwich_stuff)
    for sandwich_item in general_sandwich_stuff:
        print(sandwich_item)

make_sandwich("wheat", "pastrami", "mustard", "mayo", "hot peppers", "pickle")


# default parameter
def brew_coffee(size="medium"):
    print(f"Brewing a {size} coffee ")
brew_coffee() # this is going to call the function with default of medium
# it doesnt give an error because with no argument it falls to the default
brew_coffee("extra large") # calls the function with our extra large argument
# and overrides the default paramter

# keyword arguments **variable_name
def make_sandwich(**ingredients):
    print(ingredients)

    print(ingredients.items())
    for item, quantity in ingredients.items():
        print(f"Adding {quantity} of {item} to the sandwich")

make_sandwich(tomatoes="3 slices", lettuce="2 leaves", mayo="1 clump", salami="6 slices")


def make_someone_sandwich():
    sandwich = ""
    while True:
        sandwich_stuff = input("What would you like on your sandwich? ")
        if sandwich_stuff != "quit":
            sandwich += sandwich_stuff + " "
        else:
            break

    print(sandwich)

# make_someone_sandwich()

# returning from functions
# returning gives our function a tangible, usable output
def greet_user():
    print("Hello user!")
    # returns None
print(greet_user())

greeting = greet_user()
print(greeting) #returns None

def greet_user():
    return "Hello User!"

greet_user()
        
greeting = greet_user()
print(greeting)

def add_numbers(a,b):
    return a + b
# saves the ouput of our function to variable
result = add_numbers(5, 9)
print(result)

def multiply_nums(a, b):
    return a * b

# using the result of another funciont in a function call
print(multiply_nums(5, result))


# def getFullname(first_name, last_name, middle_name=""):
#     if middle_name:
#         print(f"{first_name} {middle_name} {last_name}")
#     else:
#         print(f"{first_name} {last_name}")
  
  
# getFullname("John", "Doe", "Doughy")

# returning solutions
def even_or_odd(num):
    if num % 2 == 0:
        return "even"
    else:
        return "odd"

print(even_or_odd(10))

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def even_or_odds(nums):
    evens_list = []
    for num in nums:
        if num % 2 == 0:
            evens_list.append(num)
    return evens_list

print(even_or_odds(numbers))
# careful what you're calling your function on
# even_or_odds(5)

# GLOBAL SCOPE
name = "Ryan" #global variable

def print_name():
    print(name) #accessing a global variable
print_name()


def even_or_odds(nums):
    evens_list = [] #function scoped variable
    for num in nums:
        # num is scoped to the for loop
        if num % 2 == 0:
            evens_list.append(num)
    print(num)
    return evens_list
    

print(even_or_odds(numbers))

# print(evens_list) #cant access varaible scoped to a function

response = input("Would you like to add subtract multiple or divide?")
num1 = input()
num2 = input()

if response == "add":
    return num1 + num2