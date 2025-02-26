#include <stdio.h>
#include <string.h>

#define MAX_STUDENTS 10
#define NAME_LENGTH 50

void sortNames(char names[MAX_STUDENTS][NAME_LENGTH], int count)
{
    char temp[NAME_LENGTH];
    for (int i = 0; i < count - 1; i++)
    {
        for (int j = i + 1; j < count; j++)
        {
            if (strcmp(names[i], names[j]) > 0)
            {
                strcpy(temp, names[i]);
                strcpy(names[i], names[j]);
                strcpy(names[j], temp);
            }
        }
    }
}

int main() {
    char nameOfStudents[MAX_STUDENTS][NAME_LENGTH];
    int n;

    printf("Enter the number of students (max 10): ");
    scanf("%d", &n);
    getchar();

    if (n > MAX_STUDENTS || n <= 0) {
        printf("Invalid number of students!\n");
        return 1;
    }

    printf("Enter %d student names:\n", n);
    for (int i = 0; i < n; i++) {
        printf("Student %d: ", i + 1);
        fgets(nameOfStudents[i], NAME_LENGTH, stdin);
        nameOfStudents[i][strcspn(nameOfStudents[i], "\n")] = '\0'; 
    }

    sortNames(nameOfStudents, n);

    printf("\nSorted List of Students:\n");
    for (int i = 0; i < n; i++) {
        printf("%s\n", nameOfStudents[i]);
    }

    return 0;
}
