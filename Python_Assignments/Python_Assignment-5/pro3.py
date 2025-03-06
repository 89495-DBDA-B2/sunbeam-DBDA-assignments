# 3) Define a function subtract() that takes two lists and returns difference (i.e. excess elements from list1). If list1 = [10, 20, 30, 40] and list2 = [30, 40, 50, 60], then result should be [10, 20].


def subtract(l1,l2):
    l3=[]
    for i in l1:
        if(i not in  l2 ):
            l3.append(i)

    print(l3)
subtract([10,20,30,40],[30,40,50,60])