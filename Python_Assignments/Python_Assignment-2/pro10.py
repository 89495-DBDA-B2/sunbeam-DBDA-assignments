# 10) Write a Python program to count the elements in a list until an element is a
# tuple.
# Sample input : list = [10, 20, 30, (40,50), 60]
# Sample output = 3


list = [10, 20, 30, (40,50), 60]

temp=-1
for i in list:
    if( type(i)!=tuple):
        temp=temp+1

print(temp)