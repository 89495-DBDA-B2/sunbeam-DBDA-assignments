# include<stdio.h>

int main(void)
{
    int a1, a2, a3, a4, a5, a;

    printf("Enter marks for subject 1: ");
    scanf("%d", &a1);
    printf("Enter marks for subject 2: ");
    scanf("%d", &a2);
    printf("Enter marks for subject 3: ");
    scanf("%d", &a3);
    printf("Enter marks for subject 4: ");
    scanf("%d", &a4);
    printf("Enter marks for subject 5: ");
    scanf("%d", &a5);

    a = a1 + a2 + a3 + a4 + a5;

    if (a >= 90) {
        printf("Grade: Ex\n");
    } else if (a >= 80) {
        printf("Grade: A\n");
    } else if (a >= 70) {
        printf("Grade: B\n");
    } else if (a >= 60) {
        printf("Grade: C\n");
    } else {
        printf("Grade: F\n");
    }

    return 0;
}