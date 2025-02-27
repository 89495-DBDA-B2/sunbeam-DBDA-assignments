# 1) Using for loop, write and run a Python program to find factorial from 0 to 10.

for n in range(11):
    def factorial(n):
        if n == 0 or n == 1:
            return 1  # Base case
        return n * factorial(n - 1)  # Recursive call

    num = n
    print(f"Factorial of {num} is {factorial(num)}")
