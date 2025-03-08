# 4) In following text count occurrence of each letter (irrespective of case). Hint: convert string to same case e.g. text.lower(). 
# Do not use Counter collection.

text = """Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation. 
Python is dynamically typed and garbage-collected. It supports multiple programming paradigms, including structured, object-oriented and functional programming."""


text=text.lower()
print(text)
l1=[]

for i in text:
    if i.isalpha():
        l1.append(i)

# print(l1)
# print()
s1=set(l1)
l2=list(s1)
# print(l2)
l3=[]
for i in l2:
    l=text.count(i)
    l3.append(l)

# print()
# print(l3)
print()

dict1={}
for i in range(len(l2)):
    dict1[l2[i]] = l3[i]

print(dict1)