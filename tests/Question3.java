/**
 * Question3.java
 * Author: luka0309
 * Borrowed from Dream In Code: http://www.dreamincode.net/forums/topic/375232-whats-wrong-with-my-code/
 */

import java.util.Scanner;
public class Question3 {
    public static void main(String[] args) {
        // TODO code application logic here
        Scanner Luka=new Scanner(System.in);
        double sum=0;double count=0;
        int[] a=new int[10];
        for(int i=1;i<=10;i++){
           System.out.println("Enter grade "+i+":");
            a[i]=Luka.nextInt();
               sum=sum+a[i]; 
            if(a[i]==-1)
                break;
            
        }
        double av=Average(sum,count);
            System.out.println(av);
            
     }
     public static double Average(double c ,double d) { 
        return  (c/d);
                
    }
}
