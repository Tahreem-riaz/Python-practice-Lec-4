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
