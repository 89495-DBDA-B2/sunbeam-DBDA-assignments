# include<stdio.h>

int main(void)
{
    int n, i = 0, num, max;
    printf("Enter how many numbers u want to compare: ");
    scanf("%d", &n);

    printf("Enter the numbers: ");
    scanf("%d", &max);

    while(i < n - 1)
    {
        printf("Enter the numbers: ");
        scanf("%d", &num);
        if (num > max)
        {
            max = num;
        }
        i++;
    }

    printf("Largest no. is %d", max);

    return 0;
}