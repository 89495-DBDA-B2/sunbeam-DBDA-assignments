# 8. Write a Python Program to find the repeated item of a tuple(Take a value from user which you want to find)


tuple1 = (12,12,12,13,14,16,18,20,21,14,18,14)

l1= [i for i in tuple1 if tuple1.count(i)>2]

s1=set(l1)
print(f"Repeated elements: {s1}")
