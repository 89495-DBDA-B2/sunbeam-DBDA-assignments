# 4] Write a program to accept three integer numbers and find its average.


# Function to calculate the average of three numbers
def calculate_average(num1, num2, num3):
    return (num1 + num2 + num3) / 3

# Taking user input
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

# Calculating average
average = calculate_average(num1, num2, num3)

# Displaying the result
print(f"The average of {num1}, {num2}, and {num3} is: {average:.2f}")
