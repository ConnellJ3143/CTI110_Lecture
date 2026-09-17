# Learning to use dictionaries
# Each entry consist of a key:value pair

# Create a dictionary where the keys are gonna be the student IDs and the values are gonna be the student names
students = {"001":"Kevin", "002":"Susie", "003":"Kate"}

# print(students)

# Give the key, have python return the value
# print(students["001"])
# print(students["002"])
# print(students["003"])

# Get the student ID from the user
student_id = input("Enter student ID: ")

# Using student ID from the user have python return the value
print(students[student_id])

##############################################################################

# add a key value pair into an existing dictionary
students["004"] = "Dion"

print(students)

# Delete a key value pair from the dictionary
del students["001"]

print()
print()
print("Kevin Graduated")
print()
print(students)