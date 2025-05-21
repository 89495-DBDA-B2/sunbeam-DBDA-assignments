// Q1) Write a java program to reverse a String 

import java.util.Scanner;

public class reverse_string{
   
    public static void main(String[] args)
    {
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter String");
        String s,rev="";
        s=sc.nextLine();

        for (int i = s.length() - 1; i >= 0; i--) 
        {
            rev += s.charAt(i);
        }
        System.out.println("Reversed String: "+rev);
        sc.close();
    }   
}
