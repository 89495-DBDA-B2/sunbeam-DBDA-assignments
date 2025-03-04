# 2.Write a Python program to find numbers divisible by nineteen or thirteen from a list of numbers using Lambda.

# Orginal list:
# [19, 65, 57, 39, 152, 639, 121, 44, 90, 190]

# Numbers of the above list divisible by nineteen or thirteen:
# [19, 65, 57, 39, 152, 190]

l1=[19, 65, 57, 39, 152, 639, 121, 44, 90, 190]

l2=list(filter(lambda m:m%13==0 or m%19==0,l1))

print(l2)