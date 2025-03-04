# 5. Create a list of tuples where each tuple contains a number and its square for numbers from 0 to 9. Solve using list comprehension.


t1=[i**2 for i in range(10)]

l2=[]
for i in range(len(t1)):
    l2.append((i,t1[i]))

print(l2)