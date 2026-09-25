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

# Create a set containing app permissions
permissions = {
    "Camera",
    "Storage",
    "Internet"
}

# Add a new permission to the set
permissions.add("Location")

# Display the updated permissions
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

# Create a set containing installed applications
applications = {
    "Chrome",
    "VS Code",
    "Spotify",
    "Discord",
    "Zoom"
}

# remove() removes the specified element
applications.remove("Spotify")

# Display the updated set
print("Installed Applications:", applications)

# ------------------------------------------

# Q4. A queue contains several task IDs.
#
#     Use pop() to remove one task.
#
#     Print:
#     - The removed task
#     - The remaining tasks

# Create a set containing task IDs
tasks = {
    "Task-101",
    "Task-102",
    "Task-103",
    "Task-104"
}

# pop() removes and returns an element from the set
removed_task = tasks.pop()

# Display the removed task
print("Removed Task:", removed_task)

# Display the remaining tasks
print("Remaining Tasks:", tasks)

