import java.util.Scanner;

public class food_menu {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        // Fixed prices for food items (index 0 unused for convenience)
        String[] items = {"", "Dosa", "Samosa", "Idli", "Vada", "Pav Bhaji", "Pizza", "Burger", "Pani Puri", "Biryani"};
        double[] prices = {0.0, 50.0, 20.0, 30.0, 25.0, 60.0, 120.0, 80.0, 20.0, 100.0};
        double totalBill = 0.0;

        while (true) {
            // Display menu
            System.out.println("\n==== Food Menu ====");
            for (int i = 1; i <= 9; i++) {
                System.out.println(i + ". " + items[i] + " - " + prices[i]+" /-Rs");
            }
            System.out.println("10. Generate Bill");
            System.out.print("Enter your choice (1-10): ");

            // Check if user entered an integer
            if (!sc.hasNextInt()) {
                System.out.println("Invalid input! Please enter a number between 1 and 10.");
                sc.next(); // consume the invalid input
                continue;
            }

            int choice = sc.nextInt();

            if (choice == 10) {
                // Generate bill and exit
                System.out.println("Total Bill: ₹" + totalBill);
                System.out.println("Thank you! Visit Again.");
                break;
            } else if (choice >= 1 && choice <= 9) {
                System.out.print("Enter quantity of " + items[choice] + ": ");
                if (!sc.hasNextInt()) {
                    System.out.println("Invalid quantity! Please enter a valid number.");
                    sc.next(); // consume invalid input
                    continue;
                }
                int qty = sc.nextInt();
                double itemTotal = prices[choice] * qty;
                totalBill += itemTotal;
                System.out.println(qty + " x " + items[choice] + " = ₹" + itemTotal);
            } else {
                System.out.println("Invalid choice! Please select from the menu.");
            }
        }

        sc.close();
    }
}
