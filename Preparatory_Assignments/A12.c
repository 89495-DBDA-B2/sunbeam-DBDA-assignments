# include<stdio.h>
# include<string.h>

void reverseString(char str[])
{
    int len = strlen(str);
    int start = 0, end = len - 1;
    char temp;

    while (start < end)
    {
        temp = str[start];
        str[start] = str[end];
        str[end] = temp;

        start++;
        end--;
    }
}

int main(void)
{
    char str[100];

    printf("Enter a string: ");
    fgets(str, sizeof(str), stdin);

    size_t len = strlen(str);
    if (len > 0 && str[len - 1] == '\n')
        {
            str[len - 1] = '\0';
        }

    reverseString(str);

    printf("Reversed string: %s\n", str);
    return 0;
}