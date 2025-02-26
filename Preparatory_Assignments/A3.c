#include<stdio.h>

int main(void)
{
    int a, sum, i, a1=0, a2=1;

    printf("Enter no. for fibonacci series: ");
    scanf("%d", &a);

    if (a <= 0)
    {
        printf("Enter a positive number greater than 0");
    }
    else
    {
        for (i=0; i<a; i++)
        {
            printf("%d ", a1);
            sum = a1 + a2;
            a1 = a2;
            a2 = sum;
            
        }
    }

    
    return 0;
 
}