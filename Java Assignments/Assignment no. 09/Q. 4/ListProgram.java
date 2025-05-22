// Q4) Write a program to create various Lists using Collection Framework. 
// Define a method to Find max number from ANY List of any numbers.  
// Hint: compareTo() 


import java.util.*;

public class ListProgram {

    // Method to find the maximum number in any list of comparable numbers
    public static <T extends Comparable<T>> T findMax(List<T> list) {
        if (list == null || list.isEmpty()) {
            return null; // Return null if the list is empty
        }
        
        T max = list.get(0); // Assume the first element is the max initially
        
        for (T element : list) {
            if (element.compareTo(max) > 0) {
                max = element; // Update max if a larger element is found
            }
        }
        
        return max;
    }

    public static void main(String[] args) {
        // Create and populate various types of lists with numbers
        List<Integer> arrayList = new ArrayList<>(Arrays.asList(10, 20, 5, 30, 25));
        List<Integer> linkedList = new LinkedList<>(Arrays.asList(50, 30, 40, 10, 60));
        List<Double> doubleList = new ArrayList<>(Arrays.asList(10.5, 20.5, 5.1, 15.2));

        // Print all lists
        System.out.println("ArrayList: " + arrayList);
        System.out.println("LinkedList: " + linkedList);
        System.out.println("DoubleList: " + doubleList);

        // Find and print the maximum value from each list
        System.out.println("Max in ArrayList: " + findMax(arrayList));
        System.out.println("Max in LinkedList: " + findMax(linkedList));
        System.out.println("Max in DoubleList: " + findMax(doubleList));
    }
}
