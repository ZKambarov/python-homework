##Task 1. Age Calculator. 
# Write a Python program to ask for a user's name and year of birth, then calculate and display their age.
#Solution:
from datetime import datetime

# Ask for the user's name
name = input("What is your name? ")

# Get the current year
current_year = datetime.now().year

# Loop until a valid year is entered
while True:
    year_of_birth_input = input("What year were you born? ")

    try:
        year_of_birth = int(year_of_birth_input)

        if year_of_birth > current_year:
            print("Year of birth cannot be in the future. Please try again.")
        elif year_of_birth < 1900:
            print("Year of birth seems too far in the past. Please try again.")
        else:
            break  # Valid year entered, exit loop
    except ValueError:
        print("Please enter a valid year of birth.")

# Calculate age
age = current_year - year_of_birth

# Display the result
print(f"Hello, {name}! You are {age} years old.")

##Task 2. Extract Car Names. 
# Extract car names from the following text:
# txt = 'LMaasleitbtui'
#Solution:
from collections import Counter

# Input string and convert to lowercase
input_letters = 'LMaasleitbtui'.lower()
letter_counts = Counter(input_letters)

# Sample list of car names (can be expanded with real data)
car_names = [
    "Tesla", "Honda", "Ford", "Buick", "Toyota", "Mazda", "Lamborghini",
    "Alfa", "Asta", "Amati", "Belta", "Kia", "BMW", "Mini", "Jeep", "Fiat", "Subaru", "Chevy",
    "Dodge", "Ram", "Lucid", "Lotus", "Acura", "Saab", "Lada", "Opel",
    "Peugeot", "Renault", "Seat", "Skoda", "Volvo", "Isuzu", "Geo", "Mitsubishi", 
    "Lasetti", "Tico", "Damas", "Matiz", "Labo", "Spark", "Cobalt", "Nexia", "Gentra",
    "Ravon", "Captiva", "Equinox", "Tracker", "Tahoe", "Trailblazer", "Traverse", "Trax",
    "Monza", "Cruze", "Onix", "Aveo", "Optra", "Menlo"
]

# Convert all car names to lowercase
car_names = [name.lower() for name in car_names]

# Function to check if a car name can be extracted from input letters
def can_build(name, available_letters):
    name_counts = Counter(name)
    for letter, count in name_counts.items():
        if available_letters[letter] < count:
            return False
    return True

# Find all car names that can be extracted
matching_names = [name.capitalize() for name in car_names if can_build(name, letter_counts)]

# Output
print("Car names that can be extracted are:", matching_names)

##Task 3. Extract Car Names. 
# Extract car names from the following text:
# txt = 'MsaatmiazD'
#Solution:
from collections import Counter

# Input string and convert to lowercase
input_letters = 'MsaatmiazD'.lower()
letter_counts = Counter(input_letters)

# Sample list of car names (can be expanded with real data)
car_names = [
    "Tesla", "Honda", "Ford", "Buick", "Toyota", "Mazda", "Lamborghini",
    "Alfa", "Asta", "Amati", "Kia", "BMW", "Mini", "Jeep", "Fiat", "Subaru", "Chevy",
    "Dodge", "Ram", "Lucid", "Lotus", "Acura", "Saab", "Lada", "Opel",
    "Peugeot", "Renault", "Seat", "Skoda", "Volvo", "Isuzu", "Geo", "Mitsubishi", 
    "Lasetti", "Tico", "Damas", "Matiz", "Labo", "Spark", "Cobalt", "Nexia", "Gentra",
    "Ravon", "Captiva", "Equinox", "Tracker", "Tahoe", "Trailblazer", "Traverse", "Trax",
    "Monza", "Cruze", "Onix", "Aveo", "Optra", "Menlo"
]

# Convert all car names to lowercase
car_names = [name.lower() for name in car_names]

# Function to check if a car name can be extracted from input letters
def can_build(name, available_letters):
    name_counts = Counter(name)
    for letter, count in name_counts.items():
        if available_letters[letter] < count:
            return False
    return True

# Find all car names that can be extracted
matching_names = [name.capitalize() for name in car_names if can_build(name, letter_counts)]

# Output
print("Car names that can be extracted are:", matching_names)

##Task 4. Extract Residence Area 
# Extract the residence area from the following text:
# txt = "I'am John. I am from London"
# #Solution:
txt = "I'am John. I am from London"

# Split the text into words
words = txt.split()

# Look for the pattern "I am from"
if "I" in words and "am" in words and "from" in words:
    i = words.index("from")
    if i + 1 < len(words):
        location = words[i + 1]
        print("Residence area:", location)
    else:
        print("Location not found after 'from'")
else:
    print("Pattern 'I am from' not found")

##Task 5. Reverse String
# Write a Python program that takes a user input string and prints it in reverse order.
# #Solution:

# Ask the user to enter a string
user_input = input("Enter a string: ")

# Reverse the string using slicing
reversed_string = user_input[::-1]

# Print the reversed string
print("Reversed string:", reversed_string)

##Task 6. Count Vowels
# Write a Python program that counts the number of vowels in a given string.
#Solution: 
# Ask the user to enter a string
user_input = input("Enter a string: ")

# Define the vowels (both lowercase and uppercase)
vowels = "aeiouAEIOU"

# Initialize a counter
vowel_count = 0

# Loop through each character in the string and check if it's a vowel
for char in user_input:
    if char in vowels:
        vowel_count += 1

# Print the result
if vowel_count == 0:
    print("There is no vowel in the string.")
else:
    print("Number of vowels:", vowel_count)

##Task 7. Find Maximum Value
# Write a Python program that takes a list of numbers as input and prints the maximum value.
# Ask the user to enter a list of numbers separated by commas
#Solution: 
user_input = input("Enter numbers separated by commas: ")

# Convert the input string into a list of numbers
try:
    number_list = [float(num.strip()) for num in user_input.split(",")]

    # Check if the list is not empty
    if number_list:
        max_value = max(number_list)
        print("Maximum value:", max_value)
    else:
        print("The list is empty.")
except ValueError:
    print("Please enter valid numbers separated by commas.")

##Task 8. Check Palindrome
# Write a Python program that checks if a given word is a palindrome (reads the same forward and backward).
#Solution: 
# Ask the user to enter a word
word = input("Enter a word: ")

# Convert to lowercase to make the check case-insensitive
cleaned_word = word.lower()

# Check if the word is the same forwards and backwards
if cleaned_word == cleaned_word[::-1]:
    print(f"'{word}' is a palindrome.")
else:
    print(f"'{word}' is not a palindrome.")

##Task 9. Extract Email Domain
# Write a Python program that extracts and prints the domain from an email address provided by the user.
#Solution: 
# Ask the user to enter an email address
email = input("Enter your email address: ")

# Check if '@' is present and extract domain
if "@" in email:
    domain = email.split("@")[1]
    print("Email domain:", domain)
else:
    print("Please enter a valid email address. '@' symbol not found.")

##Task 10.Generate Random Password
# Write a Python program to generate a random password containing letters, digits, and special characters.
#Solution: 
import random
import string

# Ask the user for the desired password length
try:
    length = int(input("Enter desired password length: "))

    if length < 4:
        print("Password length should be at least 4 characters.")
    else:
        # Define character sets
        letters = string.ascii_letters
        digits = string.digits
        special_chars = string.punctuation

        # Combine all character sets
        all_chars = letters + digits + special_chars

        # Ensure password includes at least one of each type
        password = [
            random.choice(letters),
            random.choice(digits),
            random.choice(special_chars),
        ]

        # Fill the rest of the password length
        password += random.choices(all_chars, k=length - 3)

        # Shuffle the password to avoid predictable pattern
        random.shuffle(password)

        # Join and print the password
        print("Generated password:", ''.join(password))

except ValueError:
    print("Please enter a valid number for password length.")
