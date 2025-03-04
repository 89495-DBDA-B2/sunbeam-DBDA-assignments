# 4. Calculate the sum and average of the digits present in a string Str1="Python83737@#8496"
# expected Output : sum = 55
#                   avg = 6.111

str1="Python83737@#8496"
list1=[]
for i in str1:
    if(i.isdigit()):
        list1.append(i)

add=0
for i in list1:
    add+=int(i)

avg=add/len(list1)
print(f"sum = {add}")

print(f"avg = {avg:.3f}")