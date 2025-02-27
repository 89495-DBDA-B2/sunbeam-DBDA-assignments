# 5] Write a Python function to find the maximum of three numbers.


def find_maximum(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

# Taking user input
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

# Finding the maximum number
maximum = find_maximum(num1, num2, num3)

# Displaying the result
print(f"The maximum of {num1}, {num2}, and {num3} is: {maximum}")