"""
Python Basics Demonstration
Author: Abinaya
"""

# ------------------------------
# Variables and Data Types
# ------------------------------
name = "Abinaya"
age = 20
height = 5.4
is_student = True

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is Student:", is_student)

# ------------------------------
# List
# ------------------------------
numbers = [1, 2, 3, 4, 5]
print("\nList:", numbers)

# ------------------------------
# Dictionary
# ------------------------------
student = {
    "name": "Abinaya",
    "course": "Computer Science",
    "year": 3
}
print("Dictionary:", student)

# ------------------------------
# Loop
# ------------------------------
print("\nLoop Example:")
for num in numbers:
    print(num)

# ------------------------------
# Function
# ------------------------------
def greet(user):
    return f"Hello, {user}!"

print("\nFunction Output:", greet("World"))

# ------------------------------
# Conditional
# ------------------------------
if age >= 18:
    print("\nYou are an adult.")
else:
    print("\nYou are a minor.")
