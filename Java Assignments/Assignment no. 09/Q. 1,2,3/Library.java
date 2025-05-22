import java.util.Scanner;
import java.util.HashSet;
import java.util.LinkedHashSet;
import java.util.Set;
import java.util.Date;
import java.util.List;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;

enum Category {
    FICTION, NON_FICTION, SCIENCE, HISTORY, ART;
}

class Book {
    String isbn;
    Category category;
    double price;
    Date publishDate;
    String authorName;
    int quantity;

    public Book(String isbn, Category category, double price, Date publishDate, String authorName, int quantity) {
        this.isbn = isbn;
        this.category = category;
        this.price = price;
        this.publishDate = publishDate;
        this.authorName = authorName;
        this.quantity = quantity;
    }

    @Override
    public String toString() {
        return "ISBN: " + isbn + ", Category: " + category + ", Price: " + price + ", Publish Date: " + publishDate +
                ", Author: " + authorName + ", Quantity: " + quantity;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Book book = (Book) o;
        return isbn.equals(book.isbn); // Unique based on ISBN
    }

    @Override
    public int hashCode() {
        return isbn.hashCode(); // Unique based on ISBN
    }

    // Getter for publishDate to use for sorting
    public Date getPublishDate() {
        return publishDate;
    }
}

public class Library {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Step 1: Store books in HashSet
        Set<Book> bookSet = new HashSet<>();

        // Accept at least 5 book details from the user
        for (int i = 0; i < 5; i++) {
            System.out.println("Enter details for book " + (i + 1));

            System.out.print("Enter ISBN: ");
            String isbn = scanner.nextLine();

            System.out.print("Enter Category (FICTION, NON_FICTION, SCIENCE, HISTORY, ART): ");
            Category category = Category.valueOf(scanner.nextLine().toUpperCase());

            System.out.print("Enter Price: ");
            double price = scanner.nextDouble();

            System.out.print("Enter Publish Date (yyyy-mm-dd): ");
            String publishDateString = scanner.next();
            Date publishDate = java.sql.Date.valueOf(publishDateString);

            scanner.nextLine();  // Consume the newline left-over

            System.out.print("Enter Author Name: ");
            String authorName = scanner.nextLine();

            System.out.print("Enter Quantity: ");
            int quantity = scanner.nextInt();

            // Create a new Book object
            Book book = new Book(isbn, category, price, publishDate, authorName, quantity);

            // Add the book to the HashSet (automatically handles unique ISBN)
            bookSet.add(book);

            scanner.nextLine(); // Consume the newline character after reading an integer
        }

        // Display all books in the HashSet (Note: order may not be preserved)
        System.out.println("\nBooks in the library (HashSet):");
        for (Book book : bookSet) {
            System.out.println(book);
        }

        // Step 2: Store details from HashSet into LinkedHashSet to confirm order of insertion
        Set<Book> linkedHashSet = new LinkedHashSet<>(bookSet);

        // Display books in LinkedHashSet (order of insertion will be preserved)
        System.out.println("\nBooks in the library (LinkedHashSet - Order of Insertion):");
        for (Book book : linkedHashSet) {
            System.out.println(book);
        }

        // Step 3: Sort the books based on publish date and display them
        List<Book> bookList = new ArrayList<>(bookSet);  // Convert HashSet to a List for sorting

        // Sort books by publish date
        Collections.sort(bookList, new Comparator<Book>() {
            @Override
            public int compare(Book b1, Book b2) {
                return b1.getPublishDate().compareTo(b2.getPublishDate());  // Sorting based on publish date
            }
        });

        // Display books sorted by publish date
        System.out.println("\nBooks sorted by Publish Date:");
        for (Book book : bookList) {
            System.out.println(book);
        }

        scanner.close();
    }
}
