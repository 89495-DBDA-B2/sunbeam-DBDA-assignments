# 9. Write a method in python to display the elements of list thrice if it is a number and display the element terminated with ‘#’ if it is not a number.
# Hint-: Use InBuilt Function isdigit()
# Refer below as a input:-
# mylist = [’41’,’DROND’,’Sunbeam’, ’13’,’ZARA’]


mylist = ['41','DROND','Sunbeam', '13','ZARA']
l1=[]
for i in mylist:
    if i.isdigit():
        l1.append(i*3) 
    else:
        l1.append(i+'#')
print(l1)