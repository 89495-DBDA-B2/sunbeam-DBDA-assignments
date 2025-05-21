// Q3) write a java program to count number of words in a String. 
// Hint:  You can use , trim() , length() and split() methods 

import java.util.Scanner;

public class WordCount 
{
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a string: ");
        String input = sc.nextLine();

        input = input.trim();

        if (input.isEmpty()) {
            System.out.println("Number of words: 0");
        } else {
          
            String[] words = input.split("\\s+");
            System.out.println("Number of words: " + words.length);
        }
        sc.close();
    }
}
