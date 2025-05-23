// Q.1 Create a class called Invoice that a hardware store might use to represent 
// an invoice for an item sold at the store. An Invoice should include four 
// pieces of information as instance variables—a part number (type String), a 
// part description (type String), a quantity of the item being purchased (type 
// int) and a price per item (double). Your class should have a constructor 
// that initializes the four instance variables. Provide a set and a get method 
// for each instance variable. calculates the invoice amount (i.e. multiplies the 
// quantity by the price per item), then returns the amount as a double value. 
// If the quantity is not positive, it should be set to 0. 
// If the price per item is not positive, it should be set to 0.0. 
// Write a test application named InvoiceTest that demonstrate class Invoice’s 
// capabilities. 


public class Invoice {
    private String partNumber;
    private String partDescription;
    private int quantity;
    private double pricePerItem;

    public Invoice(String partNumber, String partDescription, int quantity, double pricePerItem) {
        this.partNumber = partNumber;
        this.partDescription = partDescription;
        setQuantity(quantity);
        setPricePerItem(pricePerItem);
    }

    public String getPartNumber() {
        return partNumber;
    }

    public void setPartNumber(String partNumber) {
        this.partNumber = partNumber;
    }

    public String getPartDescription() {
        return partDescription;
    }

    public void setPartDescription(String partDescription) {
        this.partDescription = partDescription;
    }

    public int getQuantity() {
        return quantity;
    }

    public void setQuantity(int quantity) {
        this.quantity = (quantity > 0) ? quantity : 0;
    }

    public double getPricePerItem() {
        return pricePerItem;
    }

    public void setPricePerItem(double pricePerItem) {
        this.pricePerItem = (pricePerItem > 0.0) ? pricePerItem : 0.0;
    }

    public double getInvoiceAmount() {
        return quantity * pricePerItem;
    }


    public static void main(String[] args) {
        Invoice invoice = new Invoice("P123", "Hammer", 5, 12.99);

        System.out.println("Part Number: " + invoice.getPartNumber());
        System.out.println("Description: " + invoice.getPartDescription());
        System.out.println("Quantity: " + invoice.getQuantity());
        System.out.println("Price per item: $" + invoice.getPricePerItem());
        System.out.println("Invoice Amount: $" + invoice.getInvoiceAmount());

        invoice.setQuantity(-10);
        invoice.setPricePerItem(-5.50);
        System.out.println("\nAfter setting invalid values:");
        System.out.println("Quantity: " + invoice.getQuantity());
        System.out.println("Price per item: $" + invoice.getPricePerItem());
        System.out.println("Invoice Amount: $" + invoice.getInvoiceAmount());
    }
}
