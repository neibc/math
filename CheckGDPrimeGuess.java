# check whether the result of prime_number * next_prime_number + 2 is prime number or not
# ref. stackoverflow.com
# 
# java version
# 2022.07.18 by neibc96@gmail.com & GD

import java.math.BigInteger;
import java.lang.Math;
import java.util.Scanner;
import java.text.SimpleDateFormat;  
import java.util.Date;  

public class CheckGDPrimeGuess {
	public static boolean isPrime(long n) {
		if(n < 2) return false;
		if(n == 2 || n == 3) return true;
		if(n%2 == 0 || n%3 == 0) return false;
		long sqrtN = (long)Math.sqrt(n)+1;
		for(long i = 6L; i <= sqrtN; i += 6) {
			if(n%(i-1) == 0 || n%(i+1) == 0) return false;
		}
		return true;
	}
	
	public static void main(String[] args) {
		long maxnum = 1000;
		Scanner in = new Scanner(System.in);
		
		while(maxnum > 0) {
			System.out.print("\nInput long int value(>0) : ");
			maxnum = in.nextLong();
			
			SimpleDateFormat formatter = new SimpleDateFormat("dd/MM/yyyy HH:mm:ss");  
			Date sdate = new Date();  
			System.out.println("start date :" + formatter.format(sdate));  
	
			long pnum1 = 2;
			long pnum2 = 3;
			long noftrue = 0;
			long noffalse = 0;
			long tval;
			boolean pcheckresult;
			
			for(long i=3; i<=maxnum; i++) {
				if(isPrime(i) == true) {
					pnum2 = i;
					tval = pnum1 * pnum2 + 2;
					
					pcheckresult = isPrime(tval);
					
					if(pcheckresult == true) {
						noftrue++;
					} else {
						noffalse++;
					}
					
					System.out.println(Long.toString(pnum1) + " * " + Long.toString(pnum2) + " + 2 = " + Long.toString(tval) + " " + Boolean.toString(pcheckresult));
					
					pnum1 = pnum2;
					
				}
			}
			
			Date edate = new Date();  
			System.out.println("start date :" + formatter.format(sdate));  
			System.out.println("end date :" + formatter.format(edate));  
			System.out.println("-------------------------------------------------------");
			System.out.println("max number : " + Long.toString(maxnum));
			System.out.println("number of total prime numbers within maxnum : " + Long.toString(noftrue+noffalse));
			System.out.println("ratio of prime numbers within maxnum : " + Float.toString((float)(noftrue+noffalse)/(float)maxnum));
			System.out.println("\nnumber of true samples : " + Long.toString(noftrue));
			System.out.println("number of false samples : " + Long.toString(noffalse));
			System.out.println("'ratio of true samples : " + Float.toString((float)noftrue/(float)(noftrue+noffalse)));

		}
	}
}
