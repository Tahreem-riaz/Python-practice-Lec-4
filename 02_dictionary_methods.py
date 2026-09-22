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
