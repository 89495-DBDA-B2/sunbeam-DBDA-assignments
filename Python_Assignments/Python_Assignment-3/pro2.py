# 2. Write a Python program to double all numbers in a given list of integers. Use Python map,lambda function.
# list1 = [1,2,3,4,5,6,7,8,9]


list1 = [1,2,3,4,5,6,7,8,9]
double_list=lambda l:l*2
double=list(map(double_list,list1))
print(double)