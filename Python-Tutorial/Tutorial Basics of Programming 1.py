# Number assignments
one = 1
two = 2
three = 3
four = 4
five = 5

six, seven, eight = 6, 7, 8  # Added spaces after commas

# Print numbers in reverse order
print(eight)
print(seven)
print(six)
print(five)
print(four)
print(three)
print(two)
print(one)

# Variable reassignment
four = 2
print(four)

# Decimal and string variables
decimal = 9.0
print(decimal)

string_var = "Hello"  # Changed to snake_case for variable names
print(string_var)

string_var = "Hello" + " " + "1"  # String concatenation
print(string_var)

# Constant (conventionally uppercase)
PI = 3.14
print(PI)

# Function definition
def function_Name(): # Changed to snake_case for function name
    global new_var  # Declare new_var as global
    new_var = "Apple"
    print(new_var)
    return

# Call the function to see its output
function_Name()