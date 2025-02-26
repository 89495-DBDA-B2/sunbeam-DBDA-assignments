# include<stdio.h>
# include<ctype.h>
# include<string.h>

#define ALPHABET_SIZE 26

void countAlphabets(char *str, int *count)
{
    for (int i = 0; str[i] != '\0'; i++)
    {
        if (isalpha(str[i]))
        {
            count[tolower(str[i]) - 'a']++;
        }
    }
}

int main(void)
{
    char str[1000];
    int count[ALPHABET_SIZE] = {0};

    printf("Input: ");
    fgets(str, sizeof(str), stdin);
    str[strcspn(str, "\n")] = '\0';

    countAlphabets(str, count);

    printf("Output:\n");
    for (int i = 0; i < ALPHABET_SIZE; i++)
    {
        if (count[i] > 0)
        {
            printf("%c: %d\n", i + 'A', count[i]);
        }
    }

    return 0;

}