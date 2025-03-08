# 2) Write a program to sum all the values of a dictionary.
# Hint dict1 = {‘key 1’: 200, ‘key 2’: 300}
# Expected output
# Result: 500

dict1 = {'key 1': 200, 'key 2': 300}
add=0

l1=lambda m:m[1]
l2=list(map(l1,dict1.items()))
print(l2)

for i in l2:
    add+=i

print(add)


# 2nd Way to exexute

# for i in dict1.values():
#     add+=i

# print(add)