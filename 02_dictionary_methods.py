"""
========================================================
      LECTURE 04 - FILE 2: DICTIONARY METHODS
========================================================
Topics: keys(), values(), items(), get(), update()
Total Questions: 10
========================================================
"""


# ==========================================
# PART A: KEYS, VALUES & ITEMS
# ==========================================

# Q1. Create a dictionary containing information
#     about a laptop.
#
#     Use keys() to display all the keys.

laptop = {
    "brand": "HP",
    "model": "EliteBook",
    "RAM": "8GB",
    "storage": "256GB"
}

print("Laptop Keys:", laptop.keys())

# ------------------------------------------

# Q2. Create a dictionary containing five
#     countries and their capitals.
#
#     Use values() to display all capitals.

countries = {
    "Pakistan": "Islamabad",
    "France": "Paris",
    "Japan": "Tokyo",
    "Germany": "Berlin",
    "Italy": "Rome"
}

print("Capitals:", countries.values())

# ------------------------------------------

# Q3. Create a dictionary containing three
#     products and their prices.
#
#     Use items() to display each key-value pair.

products = {
    "Laptop": 80000,
    "Mouse": 2000,
    "Keyboard": 4000
}

print("Products and Prices:", products.items())

# ==========================================
# PART B: GET METHOD
# ==========================================

# Q4. Create a dictionary containing student
#     information.
#
#     Use get() to access an existing value.

student = {
    "name": "Ali",
    "age": 19,
    "semester": 3,
    "department": "Artificial Intelligence"
}

print("Student Name:", student.get("name"))

# ------------------------------------------

# ==========================================
# PART C: UPDATE METHOD
# ==========================================

# Q6. Create a dictionary containing product
#     information.
#
#     Use update() to change the price.

product = {
    "name": "Laptop",
    "price": 80000,
    "category": "Electronics"
}

print("Before update:", product)

product.update({"price": 75000})

print("After update:", product)

# ------------------------------------------

# Q7. Create a dictionary containing two
#     employee records.
#
#     Use update() to add another key-value pair
#     to one employee.

employees = {
    "employee1": {
        "name": "Ali",
        "department": "IT"
    },

    "employee2": {
        "name": "Sara",
        "department": "HR"
    }
}

employees["employee1"].update({"salary": 60000})

print("Updated Employees:", employees)

# ==========================================
# PART D: COMBINED PRACTICE
# ==========================================

# Q8. Create a dictionary containing information
#     about a course:
#
#     - course name
#     - instructor
#     - credits
#     - semester
#
#     Use keys(), values(), and items() to display
#     the information.

course = {
    "course_name": "Python Programming",
    "instructor": "Mr. Ahmed",
    "credits": 3,
    "semester": "Fall"
}

print("Course Keys:", course.keys())
print("Course Values:", course.values())
print("Course Items:", course.items())

# ------------------------------------------

# Q9. Create a dictionary for a shopping cart.
#
#     Use:
#     - get() to access an item
#     - update() to change/add information
#     - keys() to display item names

shopping_cart = {
    "Laptop": 1,
    "Mouse": 2,
    "Keyboard": 1
}

print("Mouse Quantity:", shopping_cart.get("Mouse"))

shopping_cart.update({"Mouse": 3})
shopping_cart.update({"Headphones": 1})

print("Item Names:", shopping_cart.keys())
print("Updated Cart:", shopping_cart)


# ==========================================
# PART E: CHALLENGE
# ==========================================

# Q10. Create a dictionary representing a user
#      profile.
#
#      Perform the following:
#      - Display all keys
#      - Display all values
#      - Display all key-value pairs
#      - Safely access one value using get()
#      - Update one piece of information
#
#      Print the final dictionary.

user_profile = {
    "name": "Ali",
    "age": 19,
    "city": "Lahore",
    "email": "ali@gmail.com"
}

print("Keys:", user_profile.keys())
print("Values:", user_profile.values())
print("Items:", user_profile.items())

print("User Name:", user_profile.get("name"))
user_profile.update({"city": "Islamabad"})

print("Final Dictionary:", user_profile)
