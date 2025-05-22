// Q.2)  (Credit Limit Calculator) 
// Develop a Java application that determines whether any of several 
// department-store customers has exceeded the credit limit on a 
// charge account. 
// For each customer,the following facts are available: 
// a) account number 
// b) balance at the beginning of the month 
// c) total of all items charged by the customer this month 
// d) total of all credits applied to the customer’s account this 
// month 
// e) allowed credit limit. 
// The program should input all these facts as integers, calculate 
// the new balance (= beginning balance+ charges – credits), 
// display the new balance and determine whether the new balance 
// exceeds the customer’s credit limit. For those customers whose 
// credit limit is exceeded, the program should display 
// the message "Credit limit exceeded".




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
