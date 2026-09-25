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

# ==========================================
# PART C: CLEAR
# ==========================================

# Q5. A user wants to clear all recently
#     searched topics from an application.
#
#     Create a set containing several topics.
#     Print it before and after using clear().

# Create a set containing recent searches
recent_searches = {
    "Python",
    "C++",
    "Machine Learning",
    "GitHub"
}

# Display the set before clearing
print("Searches Before Clear:", recent_searches)

# clear() removes all elements from the set
recent_searches.clear()

# Display the empty set after clearing
print("Searches After Clear:", recent_searches)

# ==========================================
# PART D: UNION
# ==========================================

# Q6. Two teams are working on a software
#     project.
#
#     Create two sets containing the skills
#     of each team.
#
#     Use union() to find all skills available
#     across both teams.

# Create a set containing Team A skills
team_a_skills = {
    "Python",
    "Git",
    "SQL"
}

# Create a set containing Team B skills
team_b_skills = {
    "JavaScript",
    "Docker",
    "Git"
}

# union() combines elements from both sets
# Duplicate values are included only once
all_skills = team_a_skills.union(team_b_skills)

# Display all available skills
print("All Team Skills:", all_skills)

# ------------------------------------------

# Q7. An online platform offers two different
#     courses.
#
#     Create a set of topics from each course.
#
#     Use union() to create a set containing
#     all topics available in both courses.

# Create a set of topics from the Python course
python_course = {
    "Variables",
    "Lists",
    "Dictionaries",
    "Functions"
}

# Create a set of topics from the Data course
data_course = {
    "SQL",
    "Databases",
    "Dictionaries",
    "Functions"
}

# Combine topics from both courses
all_topics = python_course.union(data_course)

# Display all unique topics
print("All Course Topics:", all_topics)

# ==========================================
# PART E: INTERSECTION
# ==========================================

# Q8. Two events have registered attendees.
#
#     Create two sets containing attendee names.
#
#     Use intersection() to find people who
#     registered for both events.

# Create a set of attendees for Event A
event_a = {
    "Ali",
    "Sara",
    "Ahmed",
    "Hassan"
}

# Create a set of attendees for Event B
event_b = {
    "Sara",
    "Hassan",
    "Ayesha",
    "Zain"
}

# intersection() finds values that exist
# in both sets
both_events = event_a.intersection(event_b)

# Display people registered for both events
print("Attended Both Events:", both_events)

# ------------------------------------------

# Q9. A developer knows several technologies.
#     Another developer also knows several
#     technologies.
#
#     Find the technologies they both know
#     using intersection().
