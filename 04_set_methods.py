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

# Create a set containing three project tools
tools = {
    "VS Code",
    "Git",
    "Python"
}

# add() adds a new element to the set
tools.add("GitHub")
tools.add("Docker")

# Display the updated set
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

# ==========================================
# PART B: REMOVING ELEMENTS
# ==========================================

# Q3. A computer has several installed
#     applications.
#
#     Create a set containing five applications.
#     Remove one application using remove().
#
#     Print the updated set.
