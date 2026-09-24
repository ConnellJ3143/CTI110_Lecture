# Create float variables for adoption costs
dog_fee = 30.49
penguin_fee = 4400.99
parrot_fee = 1999.99
cat_fee = 35.99

# Create integer variables
dog_quantity = 7
penguin_quantity = 2
parrot_quantity = 12
cat_quantity = 28

# Display using string-formatting
print(f"{'Animal TYPE':<16}{'Adoption Fee':<17}{'Quantity':<13}")
print("-" * 42)
print(f"{'Dog':<16}${dog_fee:<17,.2f}{dog_quantity:<13}")
print(f"{'Penguin':<16}${penguin_fee:<17,.2f}{penguin_quantity:<13}")
print(f"{'Parrot':<16}${parrot_fee:<17,.2f}{parrot_quantity:<13}")
print(f"{'Cat':<16}${cat_fee:<17,.2f}{cat_quantity:<13}")