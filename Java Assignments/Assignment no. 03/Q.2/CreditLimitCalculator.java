import java.util.Scanner;

public class CreditLimitCalculator {
    public static void main(String[] args) {
        // Scanner object to read user input
        Scanner scanner = new Scanner(System.in);
        
        // Number of customers
        System.out.print("Enter the number of customers: ");
        int numberOfCustomers = scanner.nextInt();
        
        // Process each customer
        for (int i = 1; i <= numberOfCustomers; i++) {
            System.out.println("Enter details for customer " + i + ":");
            
            // Input details for each customer
            System.out.print("Enter account number: ");
            int accountNumber = scanner.nextInt();
            
            System.out.print("Enter balance at the beginning of the month: ");
            int beginningBalance = scanner.nextInt();
            
            System.out.print("Enter total charges this month: ");
            int charges = scanner.nextInt();
            
            System.out.print("Enter total credits this month: ");
            int credits = scanner.nextInt();
            
            System.out.print("Enter allowed credit limit: ");
            int creditLimit = scanner.nextInt();
            
            // Calculate the new balance
            int newBalance = beginningBalance + charges - credits;
            
            // Display the new balance
            System.out.println("New balance for account " + accountNumber + ": " + newBalance);
            
            // Check if the credit limit is exceeded
            if (newBalance > creditLimit) {
                System.out.println("Credit limit exceeded!");
            } else {
                System.out.println("Credit limit not exceeded.");
            }
            
            System.out.println(); // Blank line for separation
        }
        
        // Close the scanner
        scanner.close();
    }
}
