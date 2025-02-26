import java.util.Scanner;

class A7
{
    public static void main(String[] args)
    {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter a number: ");
        int number = scanner.nextInt();

        System.out.println("Table");
        for (int i = 0; i <= 10; i++)
        {
            System.out.println(number + " x " + i + " = " + (number * i));
        
        }
        scanner.close();
    }
}
