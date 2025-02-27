# 6) Find and display the largest number of a list without using built-in function max(). Your program should ask the user to input values in list from keyboard.

n=int(input("Enter no of element: "))
# print(list1)

list1=[]

for i in range(n):
    ele=input("Enter Element: ")
    list1.append(ele)
max_num = list1[0]  

for num in list1:
    if num > max_num:
        max_num = num  

print("Largest number:", max_num) 