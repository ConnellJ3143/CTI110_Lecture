# Learing to use for loops
import time


# For loop needs the range function   range(start, end+1, step)
for num in range (2,11,2):
    print(num)
    time.sleep(1)


# Loop through a list

classes = ["Math", "Science", "Reading", "P.E"]

for subject in classes:
    print(subject + "!")