# 1) Given a dictionary of students and their favourite colours:
# people={'Arham':'Blue','Lisa':'Yellow',''Vinod:'Purple','Jenny':'Pink'}
# A. Find out how many students are in the list
# B. Change Lisa’s favourite colour
# C. Remove 'Jenny' and her favourite colour
# D. Sort and print students and their favourite colours alphabetically by name

people={'Arham':'Blue','Lisa':'Yellow','Vinod':'Purple','Jenny':'Pink'}

add=0
for i in people.keys():
    add=add+1

print(f"{add} Students are available in list")


people['Lisa']='Red'
print("Lisa fav colour changed..")
print(people)

people.pop('Jenny')
print("Jenny removed..")
print(people)

sorted(people.keys())
print(people)