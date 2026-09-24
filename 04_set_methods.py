"""
========================================================
           LECTURE 04 - FILE 4: SET METHODS
========================================================
Topics: Adding, Removing, Clear, Pop, Union,
        Intersection
Total Questions: 10
========================================================
"""

# ==========================================
# PART A: ADDING ELEMENTS
# ==========================================

# Q1. A software project requires several
#     programming tools.
#
#     Create a set containing three tools.
#     Use add() to add two more tools.
#
#     Print the updated set.

tools = {
    "VS Code",
    "Git",
    "Python"
}

tools.add("GitHub")
tools.add("Docker")

print("Project Tools:", tools)

# ------------------------------------------

# Q2. A mobile application has several
#     permissions.
#
#     Create a set containing three permissions.
#     Add a new permission using add().
#
#     Print the updated set.

permissions = {
    "Camera",
    "Storage",
    "Internet"
}

permissions.add("Location")

print("App Permissions:", permissions)
