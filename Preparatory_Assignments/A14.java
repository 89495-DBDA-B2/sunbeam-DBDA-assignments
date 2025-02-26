import java.util.Scanner;

public class A14
{
    public static boolean isPalidrome(String str)
    {
        str = str.replaceAll("^a-zA-Z0-9", "").toLowerCase();
        int left = 0, right = str.length() - 1;

        while(left < right)
        {
            if(str.charAt(left) != str.charAt(right))
            {
                return false;
            }
            left++;
            right--;
        }
         return true;   
    }

    public static void main(String[] args)
    {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a String: ");
        String input = scanner.nextLine();

        if (isPalidrome(input))
        {
            System.out.print("The string is a palindrome.");
        }
        else
        {
            System.out.print("The string is not a palindrome.");
        }
        scanner.close();
    }
}

