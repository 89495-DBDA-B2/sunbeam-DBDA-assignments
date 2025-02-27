# 5) Define a function overlapping() that takes two lists and returns True if they have at least one member in common, False otherwise.

def overlapping(list1,list2):
    flag=0
    for i in list1:
        for j in list2:
            if (i==j):
                flag=1
                break
            else:
                flag=0
    if(flag==1):
        print("True")
    else:
        print("False")


list1 = input("Enter first List elemets: ").split()
list2 = input("Enter second List elemets: ").split()

overlapping(list1,list2)