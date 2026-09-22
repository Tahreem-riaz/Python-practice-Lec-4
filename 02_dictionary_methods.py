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
