# 10] The marks obtained by a student in 3 different subjects are input by the user. Your
#     program should calculate the average of subjects and display the grade. The student
#     gets a grade as per the following rules:
#     Average Grade
#     90-100 A
#     80-89 B
#     70-79 C
#     60-69 D
#      0-59 F



sub1=int (input("Enter First Subject Mark: "))
sub2=int(input("Enter Second Subject Mark: "))
sub3=int(input("Enter Third Subject Mark: "))
print("second")
avg= (sub1 + sub2 + sub3) / 3

if(avg <= 100 and avg >= 90):
    print("Grade: A")
elif(avg <=89 and avg >= 80):
    print("Grade: B")
elif(avg <=79 and avg >= 70):
    print("Grade: C")
elif(avg <=69 and avg >= 60):
    print("Grade: D")  
else:
    print("Grade: F")