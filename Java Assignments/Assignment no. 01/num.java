import java.util.Scanner;

public class num{
    public static void main(String args[])
    {   
        
        System.out.println("hello");
        Scanner sc =new Scanner(System.in);
        System.out.println("Enter Num: ");

        int num=sc.nextInt();
        System.out.println("Given Num: "+num);

        System.out.println("Binary Conversion: "+Integer.toBinaryString(num));
        System.out.println("Octal Conversion: "+Integer.toOctalString(num));
        System.out.println("Hexa Conversion: "+Integer.toHexString(num));



    } 
}

