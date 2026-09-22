"""
========================================================
       LECTURE 04 - FILE 1: DICTIONARY BASICS
========================================================
Topics: Dictionaries, Key-Value Pairs, Properties,
        Accessing, Modifying, Nested Dictionaries
Total Questions: 10
========================================================
"""

# ==========================================
# PART A: CREATING DICTIONARIES
# ==========================================

# Q1. Create a dictionary containing information
#     about a book:
#
#     - title
#     - author
#     - price
#     - available
#
#     Print the complete dictionary.

book = {
    "title": "The Alchemist",
    "author": "Paulo Coelho",
    "price": 1200,
    "available": True
}
print(book)

# ------------------------------------------

# ------------------------------------------

# Q2. Create a dictionary containing information
#     about a mobile phone.
#
#     Use at least four key-value pairs.
#
#     Print each key and its corresponding value.

mobile = {
    "brand": "Samsung",
    "model": "Galaxy A07",
    "storage": "128GB",
    "price": 35000
}

print("Brand:", mobile["brand"])
print("Model:", mobile["model"])
print("Storage:", mobile["storage"])
print("Price:", mobile["price"])


# ==========================================
# PART B: ACCESSING DATA
# ==========================================

# Q3. Create a dictionary containing five
#     programming languages and their creators.
#
#     Access and print the creator of one
#     particular language using its key.

languages = {
    "Python": "Guido van Rossum",
    "C++": "Bjarne Stroustrup",
    "Java": "James Gosling",
    "JavaScript": "Brendan Eich",
    "Ruby": "Yukihiro Matsumoto"
}

print("Creator of Python:", languages["Python"])

# ------------------------------------------

# Q4. Create a student dictionary containing:
#
#     name, age, semester, department
#
#     Print:
#     - Student name
#     - Department
#     - Semester
#
#     Access each value using its key.

student = {
    "name": "Ali",
    "age": 19,
    "semester": 3,
    "department": "Artificial Intelligence"
}

print("Student Name:", student["name"])
print("Department:", student["department"])
print("Semester:", student["semester"])

# ==========================================
# PART C: MODIFYING DATA
# ==========================================

# Q5. Create a dictionary representing a product.
#
#     Change the price of the product.
#     Add a new key called "stock".
#
#     Print the dictionary before and after
#     the changes.

product = {
    "name": "Laptop",
    "price": 80000,
    "category": "Electronics"
}

print("Before changes:", product)

product["price"] = 75000
product["stock"] = 10

print("After changes:", product)

# ------------------------------------------

# Q6. Create a dictionary containing three
#     subjects and their marks.
#
#     Change the marks of one subject.
#     Add a new subject and its marks.
#
#     Print the updated dictionary.

marks = {
    "English": 80,
    "Math": 75,
    "Computer": 90
}

marks["Math"] = 85
marks["Physics"] = 78
print("Updated marks:", marks)

# ==========================================
# PART D: DICTIONARY PROPERTIES
# ==========================================

# Q7. Create a dictionary containing repeated
#     values but different keys.
#
#     Print the dictionary.
#
#     Add the same key again with a different
#     value and observe what happens.
#
#     Write your observation as a comment.

data = {
    "name": "Ali",
    "city": "Lahore",
    "country": "Lahore"
}

print(data)

data["name"] = "Ahmed"
print(data)

# Observation:
# A dictionary cannot have duplicate keys.
# If the same key is added again, its old value
# is replaced by the new value.

# ------------------------------------------

# Q8. Create a dictionary and try accessing
#     a key that does not exist.
#
#     Observe the error.
#
#     Write the error type as a comment.

student_info = {
    "name": "Ali",
    "age": 19
}

print(student_info["department"])

# Error:
# KeyError
#
# The program gives a KeyError because the
# "department" key does not exist.


# ==========================================
# PART E: NESTED DICTIONARIES
# ==========================================

# Q9. Create a nested dictionary containing
#     information about two students.
#
#     Each student should have:
#     - name
#     - semester
#     - department
#
#     Access and print the department of one
#     student.

students = {
    "student1": {
        "name": "Ali",
        "semester": 3,
        "department": "Artificial Intelligence"
    },

     "student2": {
        "name": "Sara",
        "semester": 2,
        "department": "Computer Science"
    }
}
print("Department:", students["student1"]["department"])

# ------------------------------------------

# Q10. Create a nested dictionary for a university.
#
#     Store information about:
#     - Computer Science
#     - Cyber Security
#
#     Each department should contain at least
#     two pieces of information.
#
#     Access and print one value from the
#     nested dictionary.


university = {
    "Computer Science": {
        "students": 500,
        "head": "Dr. Ahmed"
    },

    "Cyber Security": {
        "students": 300,
        "head": "Dr. Sara"
    }
}

print("CS Students:", university["Computer Science"]["students"])

# ==========================================
# END OF PRACTICE
# ==========================================
# nothing to commit