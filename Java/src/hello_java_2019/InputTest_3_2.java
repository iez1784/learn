package hello_java_2019;
import java.util.*;

/**
 * This program demonstrates console input.
 * @version 1.10 2019-1-10
 * @author ez17
 */

public class InputTest_3_2 {
	public static void main(String[] agrs)
	{
		Scanner in = new Scanner(System.in);
		
		// get first input
		System.out.println("What is your name?");
		String name = in.nextLine();
		// get second input
		System.out.println("How old are you");
		int age = in.nextInt();
		
		// display output on console
		System.out.println("Hello," + name + ". Next year, you'll be " + (age + 1) );
	}

}
