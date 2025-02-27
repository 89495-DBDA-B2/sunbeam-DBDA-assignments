
# 6] Write a Python Program Get age input from user and check if user is eligible for voting


def function1(age):
    if age >= 18:
        return "You are eligible to vote. "
    else:
        return "You are not eligible to vote. "

age = int(input("Enter your age: "))

result = function1(age)

print(result)
