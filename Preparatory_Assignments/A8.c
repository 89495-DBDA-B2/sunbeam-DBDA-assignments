#include <stdio.h>

struct Student {
    char studentName[50];
    char rollNo[20];
    int totalMarks;
};

void readStudent(struct Student *s) {
    printf("Enter student name: ");
    scanf(" %[^\n]", s->studentName);  

    printf("Enter roll number: ");
    scanf(" %s", s->rollNo);  

    printf("Enter total marks: ");
    scanf("%i", &s->totalMarks);
}

void displayStudent(struct Student s) {
    printf("Name: %s\n", s.studentName);
    printf("Roll Number: %s\n", s.rollNo);
    printf("Total Marks: %i\n", s.totalMarks);
}

int main() 
{
    int n, i;

    printf("Enter the number of students: ");
    scanf("%d", &n);

    struct Student students[n]; 
    
    for (i = 0; i < n; i++) {
        printf("\nEnter details for Student %d:\n", i + 1);
        readStudent(&students[i]);
    }

    printf("\n==== All Student Details ====\n");
    for (i = 0; i < n; i++) {
        displayStudent(students[i]);
    }

    return 0;
}
