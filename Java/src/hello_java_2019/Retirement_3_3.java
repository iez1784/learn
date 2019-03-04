package hello_java_2019;
import java.util.*;

/**
 * This program demonstrates a <code>while</code> loop.
 * @version 1.20 2019-01-09
 * @author ez17
 *
 */

public class Retirement_3_3 {
	public static void main(String[] args)
	{
		//read inputs
		Scanner in = new Scanner(System.in);
		System.out.print("How much money do you need to retire? ");
		double goal = in.nextDouble();
		
		System.out.println("How much money will you contribute every year? ");
		double payment = in.nextDouble();
		
		System.out.print("Interest rate in %:");
		double interestRate = in.nextDouble();
		
		double balance = 0;
		int years = 0;
		
		//update account balance while goal isn't reached
		while (balance < goal)
		{
			//add this year's payment and interest
			balance += payment;
			double interest = balance * interestRate / 100;
			balance += interest;
			years++;
		}
		
		System.out.println("You can retire in " + years + "years.");
	}

}
