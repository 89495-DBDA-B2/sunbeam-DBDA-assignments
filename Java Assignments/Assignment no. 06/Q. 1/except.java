//  Q1) Define a new exception, called ExceptionLineTooLong, that prints out the error message "The
//  strings is too long". Write a program that reads a String from user and calculates its length. and throws
//  an exception of type ExceptionLineTooLong in the case where a string of length is more than 80
//  characters




import java.util.Scanner;

class ExceptionLineTooLong extends Exception {
    public ExceptionLineTooLong(String message) {
        super(message);
    }
}


public class except{
    public static void main(String[] args)
    {
        Scanner sc =new Scanner(System.in);
        System.out.println("Enter String: ");
        String s=sc.nextLine();

       try
       {
            if (s.length() > 80) 
            {
                throw new ExceptionLineTooLong("The string is too long");
            } 
            else 
            {
                System.out.println("Input accepted: " + s);
            }
        } 
        catch (ExceptionLineTooLong e) 
        {
            System.out.println(e.getMessage());
        }
        finally
        {
            sc.close();
        }    
    }
    
}
