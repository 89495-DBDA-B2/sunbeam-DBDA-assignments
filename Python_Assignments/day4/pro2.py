# 2) Write a program that accepts a list from user and print the alternate element of list.

# Accept a list from the user
user_list = input("Enter elements separated by spaces: ").split()

# Print alternate elements using slicing
print("Alternate elements:", user_list[::2])
