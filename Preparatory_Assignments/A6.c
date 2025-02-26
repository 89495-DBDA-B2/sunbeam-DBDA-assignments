# include<stdio.h>
# define ROWS 10
# define COLS 10

void InputMatrix(int matrix[ROWS][COLS], int row, int col)
{
    printf("Enter elements of the matrix (%d x %d):\n", row, col);
    for (int i = 0; i < row; i++)
    {
        for (int j = 0; j < col; j++)
        {
            scanf("%d", &matrix[i][j]);
        }
        
    } 
}

void Mulitply(int matrix1[ROWS][COLS], int matrix2[ROWS][COLS], int result[ROWS][COLS], int row1, int col1, int col2)
{
    for (int i = 0; i < row1; i++)
    {
        for (int j = 0; j < col2; j++)
        {
            result[i][j]=0;
            for (int k = 0; k < col1; k++)
            {
                result[i][j] += matrix1[i][k] * matrix2[k][j];
            }
        }
    }
}

void PrintMatrix(int matrix[ROWS][COLS], int row, int col)
{
    printf("The resulting matrix is:\n");
    for (int i = 0; i < row; i++)
    {
        for (int j = 0; j < col; j++)
        {
            printf("%d ", matrix[i][j]);
        }
        printf("\n");
    }
}

int main(void)
{
    int matrix1[ROWS][COLS], matrix2[ROWS][COLS], result[ROWS][COLS];
    int row1, col1, row2, col2;
    
    printf("Enter rows and columns of first matrix: ");
    scanf("%d %d", &row1, &col1);
    printf("Enter rows and columns of second matrix: ");
    scanf("%d %d", &row2, &col2);

    if (col1 != row2)
    {
        printf("Matrix multiplication not possible. Column of first matrix must be equal to row of second matrix.\n");
        return 1;
    }

    InputMatrix(matrix1, row1, col1);
    InputMatrix(matrix2, row2, col2);

    Mulitply(matrix1, matrix2, result, row1, col1, col2);

    PrintMatrix(result, row1, col2);

    return 0;


}