# include<stdio.h>

int main(void)
{
    int a, fact = 1, i;

    printf("Enter the number for factorial: ");
    scanf("%d", &a);

    if (a<0)
    {
        printf("Factorial not available for negative numbers.");
    }
    else
    {
        for(i=1; i<=a ;i++)
        {
            fact *= i;

        }

        printf("Factorial of %d is %d", a, fact);
    }
    
    
}