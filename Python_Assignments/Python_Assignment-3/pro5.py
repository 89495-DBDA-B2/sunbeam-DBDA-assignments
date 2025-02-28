# 5. Write a Python program that adds two lists element-wise using the map() function.
#     input :   list1 = [1, 2, 3, 4, 5]
#               list2 = [5, 4, 3, 2, 1]
#     Expected Output  : [6, 6, 6, 6, 6]

list1 = [1, 2, 3, 4, 5]
list2 = [5, 4, 3, 2, 1]

l1=list(map(str,list1))
l2=list(map(str,list2))

add=list(map(lambda x,y:int(x)+int(y),l1,l2))
print(add)