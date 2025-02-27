
# 7] Write a Python program to find given number is positive ,negative or zero .


def check_number(num):
    if num > 0:
        return "The number is Positive. "
    elif num < 0:
        return "The number is Negative. "
    else:
        return "The number is Zero. "

num = float(input("Enter a number: "))


result = check_number(num)

print(result)
