# include<stdio.h>

int main(void)
{
    char c;
    int upper = 0, lower = 0, num = 0, special = 0;
    printf("Enter a character: ");

    while (1)
    {
        scanf("%c", &c);
        if (c == '\n')
            break;
        else if (c >= 'A' && c <= 'Z')
        {
            printf("%c character is a uppercase character\n", c);
            upper++;
        }

        else if (c >= 'a' && c <= 'z')
        {
            printf("%c character is a lower character\n", c);
            lower++;
        }

        else if (c >= '0' && c <= '9')
        {
            printf("%c character is a digit\n", c);
            num++;
        }

        else 
        {
            printf("%c character is a special character\n", c);
            special++;
        }

    }
    printf("No. of Uppercase letters: %d\n", upper);
    printf("No. of Lowercase letters: %d\n", lower);
    printf("No. of Digits: %d\n", num);
    printf("No. of Special letters: %d\n", special);
 
    return 0;

}