"""
========================================================
             LECTURE 04 - FILE 3: SETS
========================================================
Topics: Sets, Unique Values, Set Properties,
        Creating Empty Sets
Total Questions: 8
========================================================
"""

# ==========================================
# PART A: CREATING SETS
# ==========================================

# Q1. Create a set containing five programming
#     languages.
#
#     Print the set and its type.

languages = {
    "Python",
    "C++",
    "Java",
    "JavaScript",
    "C#"
}

print("Programming Languages:", languages)
print("Type:", type(languages))

# ------------------------------------------

# Q2. A system stores the skills of a student.
#     Some skills are entered more than once.
#
#     Create a set containing repeated skills.
#
#     Print the set and write an observation
#     about duplicate values.

skills = {
    "Python",
    "C++",
    "Python",
    "HTML",
    "C++",
    "Python"
}

print("Student Skills:", skills)

# Observation:
# Sets automatically remove duplicate values.
# Each value appears only once.

# ==========================================
# PART B: SET PROPERTIES
# ==========================================

# Q3. A university system stores student ID
#     numbers who attended a workshop.
#
#     Some students may have been recorded more
#     than once.
#
#     Create a set containing repeated IDs and
#     print the final set.

student_ids = {
    101,
    102,
    103,
    101,
    104,
    102,
    105
}

print("Unique Student IDs:", student_ids)

# Observation:
# Duplicate student IDs are automatically removed.

# ------------------------------------------

# Q4. A shopping system stores the fruits
#     selected by a customer.
#
#     Create a set containing five fruits.
#
#     Add a new fruit and then try adding a
#     fruit that already exists.
#
#     Print the set before and after.

fruits = {
    "Apple",
    "Banana",
    "Mango",
    "Orange",
    "Grapes"
}

print("Before adding:", fruits)

fruits.add("Watermelon")
fruits.add("Apple")

print("After adding:", fruits)

# Observation:
# Watermelon is added because it is new.
# Apple is not added again because it already exists.

# ==========================================
# PART C: EMPTY SETS
# ==========================================

# Q5. Create an empty set.
#
#     Check and print its type.

empty_set = set()

print("Empty Set:", empty_set)
print("Type:", type(empty_set))

# ------------------------------------------

# Q6. Create an empty dictionary and an empty
#     set.
#
#     Print the type of both.
#
#     Write a comment explaining how you can
#     distinguish an empty set from an empty
#     dictionary.

empty_dictionary = {}
empty_set = set()

print("Empty Dictionary Type:", type(empty_dictionary))
print("Empty Set Type:", type(empty_set))

# Observation:
# {} creates an empty dictionary.
# set() creates an empty set.
# Therefore, we use set() when we need an empty set.

# ==========================================
# PART D: PRACTICAL SETS
# ==========================================

# Q7. A university wants to know which cities
#     students come from.
#
#     Create a set containing city names with
#     some duplicate cities.
#
#     Print the final set.
#
#     Write a comment explaining why a set is
#     useful in this situation.

cities = {
    "Lahore",
    "Karachi",
    "Islamabad",
    "Lahore",
    "Multan",
    "Karachi"
}

print("Unique Cities:", cities)

# Observation:
# A set is useful because it stores only unique
# city names and removes duplicates automatically.

# ------------------------------------------

# Q8. A system stores the allowed user roles.
#
#     Create a set containing:
#     - Admin
#     - Teacher
#     - Student
#     - Guest
#
#     Try adding "Student" again.
#
#     Print the final set and explain why sets
#     are useful for storing unique values.

roles = {
    "Admin",
    "Teacher",
    "Student",
    "Guest"
}

roles.add("Student")