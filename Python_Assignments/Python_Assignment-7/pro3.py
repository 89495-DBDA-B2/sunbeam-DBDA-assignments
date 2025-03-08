# 3.
# Create a class 'Student' with rollno, studentName, course ,dictionary of marks(subjectName -marks [5]).
# Provide following functionalities
# A. initializer
# B. override __str__ method
# C. accept student data
# D. Print student data
# E. accept records of 5 students and Print it


class Student:
    def __init__(self, rollno, studentName, course, marks):
        # Initializer to set the student data
        self.rollno = rollno
        self.studentName = studentName
        self.course = course
        self.marks = marks  # A dictionary where the subject names are the keys and the marks are the values
    
    def __str__(self):
        # Override __str__ method to print the student data
        marks_str = ", ".join([f"{subject}: {marks}" for subject, marks in self.marks.items()])
        return f"Roll Number: {self.rollno}, Name: {self.studentName}, Course: {self.course}, Marks: {marks_str}"

    def accept_data(self):
        # Accept student data
        self.rollno = input("Enter roll number: ")
        self.studentName = input("Enter student name: ")
        self.course = input("Enter course: ")
        
        self.marks = {}
        for _ in range(5):
            subject_name = input("Enter subject name: ")
            subject_marks = int(input(f"Enter marks for {subject_name}: "))
            self.marks[subject_name] = subject_marks
    
    def print_data(self):
        # Print the student data
        print(self)
        

# Accept and print records for 5 students
students = []
for i in range(5):
    print(f"Enter data for student {i+1}:")
    student = Student("", "", "", {})
    student.accept_data()
    students.append(student)

# Print all students' data
for student in students:
    student.print_data()
