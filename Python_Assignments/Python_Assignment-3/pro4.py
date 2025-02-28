# 4. Write a Python program that calculates the sum of the squares of all odd numbers in a list of integers using map() and filter()

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

odd=list(filter(lambda m:m%2!=0,numbers))

sq=list(map(lambda m:m**2,odd))

add=0
for i in sq:
    add=add+i
print(add)