# 6) Write a program in Python to find out the frequency of each number in stored in a list using a python dictionary.
# Example
# List1 = [1,2,3,4,5,6,7,8,9,7,6,2,4,2,5,23,6,4]
# Output ={1: 1, 2: 3, 3: 1, 4: 3, 5: 2, 6: 3, 7: 2, 8: 1, 9: 1, 23: 1}

# Given list
List1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 7, 6, 2, 4, 2, 5, 23, 6, 4]

# Initialize an empty dictionary to store the frequency of each number
frequency = {}

# Iterate through the list
for num in List1:
    # If the number is already a key in the dictionary, increment its value
    if num in frequency:
        frequency[num] += 1
    # If the number is not in the dictionary, add it with value 1
    else:
        frequency[num] = 1

# Print the frequency dictionary
print(frequency)
