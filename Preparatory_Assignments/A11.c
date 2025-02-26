#include <stdio.h>
#include <string.h>

struct Employee
{
    char first_name[50];
    char last_name[50];
    double monthly_salary;
};

void emp_init(struct Employee *e, char *first, char *last, double salary)
{
    strcpy(e->first_name, first);
    strcpy(e->last_name, last);
    e->monthly_salary = (salary > 0) ? salary : salary;
}

void set_salary(struct Employee *e, double sal)
{
    if (sal > 0)
    {
        e->monthly_salary = sal;
    }
}

void emp_display(struct Employee *e)
{
    printf("Employee: %s %s\n", e->first_name, e->last_name);
    printf("Monthly Salary: %.2f\n", e->monthly_salary);
    printf("Yearly Salary: %.2f\n", e->monthly_salary * 12);
}

int main(void)
{
    struct Employee emp1, emp2;

    emp_init(&emp1, "Abdul Mateen", "Mulla", 5000);
    emp_init(&emp2, "Abdul ", "Gh", 6000);

    printf("\nStarting Salaries:\n\n");
    emp_display(&emp1);
    printf("\n");
    emp_display(&emp2);

    set_salary(&emp1, emp1.monthly_salary * 1.10);
    set_salary(&emp2, emp2.monthly_salary * 1.10);

    printf("\nAfter 10%% Raise:\n\n");
    emp_display(&emp1);
    printf("\n");
    emp_display(&emp2);

}