"""
========================================================
          LECTURE 04 - FILE 5: MINI PROJECT
========================================================
Project: Student Course & Skill Manager

Concepts Used:
- Dictionaries
- Key-Value Pairs
- Dictionary Access
- Dictionary Modification
- Nested Dictionaries
- keys()
- values()
- items()
- get()
- update()
- Sets
- add()
- remove()
- union()
- intersection()
========================================================
"""

print("=" * 60)
print("           STUDENT COURSE & SKILL MANAGER")
print("=" * 60)

# ==========================================
# STEP 1: STUDENT INFORMATION
# ==========================================

# Create a dictionary containing student information.
student = {
    "Name": "Tahreem",
    "Student ID": "BSAI-005",
    "Semester": 3,
    "Department": "Artificial Intelligence"
}
print("\nStudent Information:")
print(student)

# ==========================================
# STEP 2: COURSE INFORMATION
# ==========================================

# Create a dictionary containing courses
# and their instructors.

courses = {
    "Programming Fundamentals": "Waheed Javed",
    "Discrete Structures": "Kashif Jillani",
    "Calculus": "Ali Raza",
    "Artificial Intelligence": "Sara Ahmed"
}

# ==========================================
# STEP 3: DISPLAY INFORMATION
# ==========================================

print("\nCourse Names:")

# keys() returns all course names.
print(courses.keys())

print("\nInstructors:")

# values() returns all instructor names.
print(courses.values())
