'''
3] Write a program to accept a 4 digit number and
   a. Display face value of each decimal digit
   b. Display place value of each decimal digit
   c. Display no in reverse order by changing decimal place values.
   
   If user enters a 4 digit number 9361 output should be
   a. 9 3 6 1
   b. 9361 = 9 000 + 300 + 60 + 9
   c. 1639 
   
   '''
   
num=(input("Enter 4 Digit Number: "))
# for i in num:
#     print(i,end=" ")
    
    
    
print()
l=len(num)
print(l)
for i in num:
   for j in l:
      print(i,j)
      l-=1



num=int(num)
def rev(n):
   rev=0
   while(n>0):
      digit=n %10
      rev=rev*10 +digit
      n=n//10
   return rev
revn=rev(num)   
print("Reverse Number: ",revn)