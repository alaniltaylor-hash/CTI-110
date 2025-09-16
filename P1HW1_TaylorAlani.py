# Alani Taylor
# 9/16/2025
# P1HW1
# Get numeric input from user and perform math calculations
print()
print()
print()
print("---------Calculating Exponents----------")
print()
print()

# Get base value (int) from the user
base_value = int(input("Enter an integer as the base value: "))

# Get exponent (int) from the user
exponent = int(input("Enter an integer as the exponent: "))

# Perform the exponent math
solution = base_value**exponent
# Display results to user

print(base_value, "raised to the power of", exponent, "is", solution,"!!")
print()
print()
print()
print("---------Addition and Subtraction----------")
print()
print()
print()

# Get three integers from the user

starting_int = int(input("Enter a starting integer: "))
adding_int = int(input("Enter an integer to add: "))
subtracting_int = int(input("Enter an integer to subtract: "))

# Show the results to the user
print(starting_int, "+", adding_int, "-", subtracting_int, "is equal to", starting_int + adding_int - subtracting_int)

