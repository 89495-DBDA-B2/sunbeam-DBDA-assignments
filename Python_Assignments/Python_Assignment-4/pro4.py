
# 4. Python program to create a list of tuples from given list having number and its cube in each tuple.
# I/P-[1,2,5,6]  Output-[(1, 1), (2, 8), (5, 125), (6, 216)]

l1=[1,2,5,6]

t1=lambda m:m**3

new_list=list(map(t1,l1))

l2=[]
for i in range(len(l1)):
    l2.append((l1[i],new_list[i]))

print(l2)