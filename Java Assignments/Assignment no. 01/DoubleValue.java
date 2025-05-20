import java.util.Scanner;

public class DoubleValue {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double d1, d2;

        System.out.print("Enter num1: ");
        if (!sc.hasNextDouble()) {
            System.out.println("Error: Enter a double number only.");
            sc.close();
            return;
        }
        d1 = sc.nextDouble();

        System.out.print("Enter num2: ");
        if (!sc.hasNextDouble()) {
            System.out.println("Error: Enter a double number only.");
            sc.close();
            return;
        }
        d2 = sc.nextDouble();

        System.out.println("num1: " + d1);
        System.out.println("num2: " + d2);

        double average = (d1 + d2) / 2;
        System.out.println("Average: " + average);

        sc.close();
    }
}
