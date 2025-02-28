# 3. Write a Python program to convert a given list of integers and a tuple of integers into a list  of strings.Use Python map. one list one tuple list of string ele


l1=[1,2,3]
t1=(4,5,6)
l2=list(map(str,t1))
l3=list(map(str,l1))
print(l3+l2)
