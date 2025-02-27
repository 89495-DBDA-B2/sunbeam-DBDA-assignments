# 7) Write a function filter_long_words() that takes a list of words and an integer len and returns the list of words that are longer than len.


def filter_long_words(list,len):
    list2=[]
    temp=0
    for i in list:
        for j in i:
            temp=temp+1
            
        if temp>len:
            list2.append(i)
            temp=0
    print(list2)

list=[]
for i in range(3):
    i=input("Enter Word: ")
    list.append(i)
len=int(input("Enter Length of word:"))

filter_long_words(list,len)