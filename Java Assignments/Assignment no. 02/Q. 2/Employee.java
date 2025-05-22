// Q.2 Create a class called Employee that includes three instance variables—a 
// first name (type String), a last name (type String) and a monthly salary 
// (double). Provide a constructor that initializes the three instance variables. 
// Provide a set and a get method for each instance variable. If the monthly 
// salary is not positive, do not set its value. Write a test application named 
// EmployeeTest that demonstrates class Employee’s capabilities. Create two 
// Employee objects and display each object’s yearly salary. Then give each 
// Employee a 10% raise and display each Employee’s yearly salary again. 



public class Employee {
    private String firstName;
    private String lastName;
    private double monthlySalary;

    public Employee(String firstName, String lastName, double monthlySalary) {
        this.firstName = firstName;
        this.lastName = lastName;
        setMonthlySalary(monthlySalary);
    }

    public String getFirstName() {
        return firstName;
    }
    public void setFirstName(String firstName) {
        this.firstName = firstName;
    }
    public String getLastName() {
        return lastName;
    }
    public void setLastName(String lastName) {
        this.lastName = lastName;
    }
    public double getMonthlySalary() {
        return monthlySalary;
    }
    public void setMonthlySalary(double monthlySalary) {
        if (monthlySalary > 0.0) {
            this.monthlySalary = monthlySalary;
        }
    }
    public double getYearlySalary() {
        return monthlySalary * 12;
    }
    public void giveRaise(double percent) {
        if (percent > 0) {
            monthlySalary += monthlySalary * (percent / 100);
        }
    }

    public static void main(String[] args) {
        Employee emp1 = new Employee("John", "Doe", 3000);
        Employee emp2 = new Employee("Jane", "Smith", 4000);

        System.out.println(emp1.getFirstName() + " " + emp1.getLastName() + " yearly salary: $" + emp1.getYearlySalary());
        System.out.println(emp2.getFirstName() + " " + emp2.getLastName() + " yearly salary: $" + emp2.getYearlySalary());

        emp1.giveRaise(10);
        emp2.giveRaise(10);

        System.out.println("\nAfter 10% raise:");
        System.out.println(emp1.getFirstName() + " " + emp1.getLastName() + " yearly salary: $" + emp1.getYearlySalary());
        System.out.println(emp2.getFirstName() + " " + emp2.getLastName() + " yearly salary: $" + emp2.getYearlySalary());
    }
}
