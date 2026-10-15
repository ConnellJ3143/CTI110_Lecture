# Learning about while loops

# while loop commonly has a control variable
run_again = "yes"

while run_again == "yes":
    print()
    print("Program is running!")
    # Get a new value for run_again from the user
    run_again = input("Run the program again? ")

# Loop breaks here
print("Program has ended, goodbye!")


# Force the while loop to run three times

num = 1
while num <= 3:
    print(num)
    # Increment num by 1
    num = num + 1