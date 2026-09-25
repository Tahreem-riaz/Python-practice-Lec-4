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

print("\nCourse and Instructor Pairs:")

# items() returns both keys and values together.
for course, instructor in courses.items():
    print(course, "->", instructor)

print("\nComplete Student Information:")

# Display each student key and value.
for key, value in student.items():
    print(key, ":", value)


# ==========================================
# STEP 4: UPDATE INFORMATION
# ==========================================

# update() can change an existing value
# and add a new key-value pair.

student.update({
    "Semester": 4,
    "Email": "student@example.com"
})

print("\nUpdated Student Information:")

for key, value in student.items():
    print(key, ":", value)

# ==========================================
# STEP 5: SAFE ACCESS
# ==========================================

# get() safely accesses an existing key.
student_name = student.get("Name")

print("\nStudent Name:", student_name)

# get() returns the default message if
# the requested key does not exist.
phone = student.get("Phone", "Phone number not available")

print("Phone:", phone)

# ==========================================
# STEP 6: STUDENT SKILLS
# ==========================================

# Create a set containing the student's
# programming and technical skills.

student_skills = {
    "Python",
    "C++",
    "HTML",
    "Git"
}

print("\nOriginal Student Skills:", student_skills)

# add() adds a new skill to the set.
student_skills.add("SQL")

print("After Adding SQL:", student_skills)

# remove() removes the specified skill.
student_skills.remove("HTML")

print("After Removing HTML:", student_skills)

# ==========================================
# STEP 7: SKILL COMPARISON
# ==========================================

# Create a set containing skills required
# for a particular project.

required_skills = {
    "Python",
    "SQL",
    "JavaScript",
    "Git"
}

# union() combines all unique skills
# from both sets.
all_skills = student_skills.union(required_skills)

# intersection() finds skills that exist
# in both sets.
shared_skills = student_skills.intersection(required_skills)

print("\nRequired Project Skills:", required_skills)
print("All Available Skills:", all_skills)
print("Shared Skills:", shared_skills)

# ==========================================
# STEP 8: NESTED DICTIONARY
# ==========================================

# Create a nested dictionary containing
# information about two courses.

course_details = {
    "Programming Fundamentals": {
        "Instructor": "Waheed Javed",
        "Credits": 3,
        "Skills": {"C++", "Programming", "Problem Solving"}
    },

    "Artificial Intelligence": {
        "Instructor": "Sara Ahmed",
        "Credits": 3,
        "Skills": {"Python", "Machine Learning", "Data Analysis"}
    }
}

print("\nNested Course Information:")

# Access information from the nested dictionary.
