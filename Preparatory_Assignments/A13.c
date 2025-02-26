# include<stdio.h>
# include<string.h>

#define SIZE 6

int main(void)
{
    char *arr[SIZE] = {"apple", "banana", "orange", "apple", "grape", "banana"};
    int dup[SIZE] = {0};

    printf("Duplicate strings\n");

    for (int i = 0; i < SIZE; i++)
    {
        if (dup[i])
            continue;
        for (int j = i + 1; j<SIZE; j++)
        {
            if (strcmp(arr[i], arr[j]) == 0)
            {
                if (!dup[i])
                {
                    printf("%s\n", arr[i]);
                    dup[i] = 1;
                }
                dup[j] = 1;
            }
            
        }
    }

    return 0;
}