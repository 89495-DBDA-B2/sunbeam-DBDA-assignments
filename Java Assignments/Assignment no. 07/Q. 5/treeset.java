// Q5) Write a Java program to create a new tree set, add some colors (string) 
// and print out the tree set 


import java.util.*;

public class treeset {
    public static void main(String[] args) {
        // Create a new TreeSet to store color names
        Set<String> colors = new TreeSet<>();

        // Add some color names to the TreeSet
        colors.add("Blue");
        colors.add("Red");
        colors.add("Green");
        colors.add("Yellow");
        colors.add("Pink");
        colors.add("Orange");

        // Print out the TreeSet (elements will be sorted automatically)
        System.out.println("TreeSet of Colors: " + colors);
    }
}
