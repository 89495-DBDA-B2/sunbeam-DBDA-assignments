# Initialize the dictionary to store EVEN and ODD numbers
number_dict = {'EVEN': [], 'ODD': []}

# Read 6 numbers from the user and categorize them
for _ in range(6):
    # Read a number from the user
    num = int(input("Enter a number: "))
    
    # Check if the number is even or odd and append it to the respective list
    if num % 2 == 0:
        number_dict['EVEN'].append(num)
    else:
        number_dict['ODD'].append(num)

# Print the resulting dictionary
print(number_dict)
